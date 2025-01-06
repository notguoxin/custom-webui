<script lang="ts">
	import { toast } from 'svelte-sonner';

	import DOMPurify from 'dompurify';
	import { marked } from 'marked';

	import { getContext, tick } from 'svelte';
	const i18n = getContext('i18n');

	import ChatBubble from '$lib/components/icons/ChatBubble.svelte';
	import LightBlub from '$lib/components/icons/LightBlub.svelte';
	import Markdown from '../Messages/Markdown.svelte';
	import Skeleton from '../Messages/Skeleton.svelte';

	export let id = '';
	export let model = null;
	export let messages = [];
	export let onAdd = () => {};

	let floatingInput = false;

	let selectedText = '';
	let floatingInputValue = '';

	let prompt = '';
	let responseContent = null;
	let responseDone = false;

	const autoScroll = async () => {
		// Scroll to bottom only if the scroll is at the bottom give 50px buffer
		const responseContainer = document.getElementById('response-container');
		if (
			responseContainer.scrollHeight - responseContainer.clientHeight <=
			responseContainer.scrollTop + 50
		) {
			responseContainer.scrollTop = responseContainer.scrollHeight;
		}
	};

	const addHandler = async () => {
		const messages = [
			{
				role: 'user',
				content: prompt
			},
			{
				role: 'assistant',
				content: responseContent
			}
		];

		onAdd({
			modelId: model,
			parentId: id,
			messages: messages
		});
	};

	export const closeHandler = () => {
		responseContent = null;
		responseDone = false;
		floatingInput = false;
		floatingInputValue = '';
	};
</script>

<div
	id={`floating-buttons-${id}`}
	class="absolute rounded-lg mt-1 text-xs z-[9999]"
	style="display: none"
>
		<div class="bg-white dark:bg-gray-850 dark:text-gray-100 rounded-xl shadow-xl w-80 max-w-full">
			<div
				class="bg-gray-50/50 dark:bg-gray-800 dark:text-gray-100 text-medium rounded-xl px-3.5 py-3 w-full"
			>
				<div class="font-medium">
					<Markdown id={`${id}-float-prompt`} content={prompt} />
				</div>
			</div>

			<div
				class="bg-white dark:bg-gray-850 dark:text-gray-100 text-medium rounded-xl px-3.5 py-3 w-full"
			>
				<div class=" max-h-80 overflow-y-auto w-full markdown-prose-xs" id="response-container">
					{#if responseDone}
						<div class="flex justify-end pt-3 text-sm font-medium">
							<button
								class="px-3.5 py-1.5 text-sm font-medium bg-black hover:bg-gray-900 text-white dark:bg-white dark:text-black dark:hover:bg-gray-100 transition rounded-full"
								on:click={addHandler}
							>
								{$i18n.t('Add')}
							</button>
						</div>
					{/if}
				</div>
			</div>
		</div>
</div>
