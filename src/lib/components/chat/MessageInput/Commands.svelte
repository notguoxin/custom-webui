<script>
	import { createEventDispatcher, onMount } from 'svelte';
	import { toast } from 'svelte-sonner';

	const dispatch = createEventDispatcher();

	import { removeLastWordFromString } from '$lib/utils';

	import Models from './Commands/Models.svelte';
	import Spinner from '$lib/components/common/Spinner.svelte';

	export let prompt = '';
	export let files = [];

	let loading = false;
	let commandElement = null;

	export const selectUp = () => {
		commandElement?.selectUp();
	};

	export const selectDown = () => {
		commandElement?.selectDown();
	};

	let command = '';
	$: command = prompt?.split('\n').pop()?.split(' ')?.pop() ?? '';

	let show = false;

	$: if (show) {
		init();
	}

	const init = async () => {
		loading = true;
		loading = false;
	};
</script>

{#if show}
	{#if !loading}
	{:else}
		<div
			id="commands-container"
			class="px-2 mb-2 text-left w-full absolute bottom-0 left-0 right-0 z-10"
		>
			<div class="flex w-full rounded-xl border border-gray-50 dark:border-gray-850">
				<div
					class="max-h-60 flex flex-col w-full rounded-xl bg-white dark:bg-gray-900 dark:text-gray-100"
				>
					<Spinner />
				</div>
			</div>
		</div>
	{/if}
{/if}
