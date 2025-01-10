<script lang="ts">
	import Switch from '$lib/components/common/Switch.svelte';
	import Tooltip from '$lib/components/common/Tooltip.svelte';
	import { getContext, createEventDispatcher } from 'svelte';

	const dispatch = createEventDispatcher();

	const i18n = getContext('i18n');

	export let admin = false;

	export let params = {
		// Advanced
		stream_response: null, // Set stream responses for this model individually
		seed: null,
		stop: null,
		temperature: null,
		frequency_penalty: null,
		repeat_last_n: null,
		mirostat: null,
		mirostat_eta: null,
		mirostat_tau: null,
		top_k: null,
		top_p: null,
		min_p: null,
		tfs_z: null,
		num_ctx: null,
		num_batch: null,
		num_keep: null,
		max_tokens: null,
		use_mmap: null,
		use_mlock: null,
		num_thread: null,
		num_gpu: null,
		template: null
	};

	let customFieldName = '';
	let customFieldValue = '';

	$: if (params) {
		dispatch('change', params);
	}
</script>

<div class=" space-y-1 text-xs pb-safe-bottom">

		<div class=" py-0.5 w-full justify-between">
			<Tooltip
				content={$i18n.t(
					'Set the number of worker threads used for computation. This option controls how many threads are used to process incoming requests concurrently. Increasing this value can improve performance under high concurrency workloads but may also consume more CPU resources.'
				)}
				placement="top-start"
				className="inline-tooltip"
			>
				<div class="flex w-full justify-between">
					<div class=" self-center text-xs font-medium">
						{$i18n.t('num_thread (Ollama)')}
					</div>

					<button
						class="p-1 px-3 text-xs flex rounded transition flex-shrink-0 outline-none"
						type="button"
						on:click={() => {
							params.num_thread = (params?.num_thread ?? null) === null ? 2 : null;
						}}
					>
						{#if (params?.num_thread ?? null) === null}
							<span class="ml-2 self-center">{$i18n.t('Default')}</span>
						{:else}
							<span class="ml-2 self-center">{$i18n.t('Custom')}</span>
						{/if}
					</button>
				</div>
			</Tooltip>

			{#if (params?.num_thread ?? null) !== null}
				<div class="flex mt-0.5 space-x-2">
					<div class=" flex-1">
						<input
							id="steps-range"
							type="range"
							min="1"
							max="256"
							step="1"
							bind:value={params.num_thread}
							class="w-full h-2 rounded-lg appearance-none cursor-pointer dark:bg-gray-700"
						/>
					</div>
					<div class="">
						<input
							bind:value={params.num_thread}
							type="number"
							class=" bg-transparent text-center w-14"
							min="1"
							max="256"
							step="1"
						/>
					</div>
				</div>
			{/if}
		</div>

		<div class=" py-0.5 w-full justify-between">
			<Tooltip
				content={$i18n.t(
					'Set the number of GPU devices used for computation. This option controls how many GPU devices (if available) are used to process incoming requests. Increasing this value can significantly improve performance for models that are optimized for GPU acceleration but may also consume more power and GPU resources.'
				)}
				placement="top-start"
				className="inline-tooltip"
			>
				<div class="flex w-full justify-between">
					<div class=" self-center text-xs font-medium">
						{$i18n.t('num_gpu (Ollama)')}
					</div>

					<button
						class="p-1 px-3 text-xs flex rounded transition flex-shrink-0 outline-none"
						type="button"
						on:click={() => {
							params.num_gpu = (params?.num_gpu ?? null) === null ? 0 : null;
						}}
					>
						{#if (params?.num_gpu ?? null) === null}
							<span class="ml-2 self-center">{$i18n.t('Default')}</span>
						{:else}
							<span class="ml-2 self-center">{$i18n.t('Custom')}</span>
						{/if}
					</button>
				</div>
			</Tooltip>

			{#if (params?.num_gpu ?? null) !== null}
				<div class="flex mt-0.5 space-x-2">
					<div class=" flex-1">
						<input
							id="steps-range"
							type="range"
							min="0"
							max="256"
							step="1"
							bind:value={params.num_gpu}
							class="w-full h-2 rounded-lg appearance-none cursor-pointer dark:bg-gray-700"
						/>
					</div>
					<div class="">
						<input
							bind:value={params.num_gpu}
							type="number"
							class=" bg-transparent text-center w-14"
							min="0"
							max="256"
							step="1"
						/>
					</div>
				</div>
			{/if}
		</div>

		<!-- <div class=" py-0.5 w-full justify-between">
			<div class="flex w-full justify-between">
				<div class=" self-center text-xs font-medium">{$i18n.t('Template')}</div>

				<button
					class="p-1 px-3 text-xs flex rounded transition flex-shrink-0 outline-none"
					type="button"
					on:click={() => {
						params.template = (params?.template ?? null) === null ? '' : null;
					}}
				>
					{#if (params?.template ?? null) === null}
						<span class="ml-2 self-center">{$i18n.t('Default')}</span>
					{:else}
						<span class="ml-2 self-center">{$i18n.t('Custom')}</span>
					{/if}
				</button>
			</div>

			{#if (params?.template ?? null) !== null}
				<div class="flex mt-0.5 space-x-2">
					<div class=" flex-1">
						<textarea
							class="px-3 py-1.5 text-sm w-full bg-transparent border dark:border-gray-600 outline-none rounded-lg -mb-1"
							placeholder={$i18n.t('Write your model template content here')}
							rows="4"
							bind:value={params.template}
						/>
					</div>
				</div>
			{/if}
		</div> -->
</div>
