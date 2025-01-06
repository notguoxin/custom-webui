<script lang="ts">
	import { toast } from 'svelte-sonner';

	import { config, functions, models, settings, user } from '$lib/stores';
	import { createEventDispatcher, onMount, getContext, tick } from 'svelte';

	import {
		getUserValvesSpecById as getFunctionUserValvesSpecById,
		getUserValvesById as getFunctionUserValvesById,
		updateUserValvesById as updateFunctionUserValvesById,
		getFunctions
	} from '$lib/apis/functions';

	import Tooltip from '$lib/components/common/Tooltip.svelte';
	import Spinner from '$lib/components/common/Spinner.svelte';
	import Valves from '$lib/components/common/Valves.svelte';

	const dispatch = createEventDispatcher();

	const i18n = getContext('i18n');

	export let show = false;

	let selectedId = '';

	let loading = false;

	let valvesSpec = null;
	let valves = {};

	let debounceTimer;

	const debounceSubmitHandler = async () => {
		if (debounceTimer) {
			clearTimeout(debounceTimer);
		}

		// Set a new timer
		debounceTimer = setTimeout(() => {
			submitHandler();
		}, 500); // 0.5 second debounce
	};

	const getUserValves = async () => {
		loading = true;
		if (valvesSpec) {
			// Convert array to string
			for (const property in valvesSpec.properties) {
				if (valvesSpec.properties[property]?.type === 'array') {
					valves[property] = (valves[property] ?? []).join(',');
				}
			}
		}

		loading = false;
	};

	const submitHandler = async () => {
		if (valvesSpec) {
			// Convert string to array
			for (const property in valvesSpec.properties) {
				if (valvesSpec.properties[property]?.type === 'array') {
					valves[property] = (valves[property] ?? '').split(',').map((v) => v.trim());
				}
			}
		}
	};

	$: if (tab) {
		selectedId = '';
	}

	$: if (selectedId) {
		getUserValves();
	}

	$: if (show) {
		init();
	}

	const init = async () => {
		loading = true;
		loading = false;
	};
</script>

{#if show && !loading}
	<form
		class="flex flex-col h-full justify-between space-y-3 text-sm"
		on:submit|preventDefault={() => {
			submitHandler();
			dispatch('save');
		}}
	>
		<div class="flex flex-col">
			{#if selectedId}
				<hr class="dark:border-gray-800 my-1 w-full" />

				<div class="my-2 text-xs">
					{#if !loading}
						<Valves
							{valvesSpec}
							bind:valves
							on:change={() => {
								debounceSubmitHandler();
							}}
						/>
					{:else}
						<Spinner className="size-5" />
					{/if}
				</div>
			{/if}
		</div>
	</form>
{:else}
	<Spinner className="size-4" />
{/if}
