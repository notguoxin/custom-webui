<script>
	import { onDestroy, onMount, tick, getContext, createEventDispatcher } from 'svelte';
	const i18n = getContext('i18n');
	const dispatch = createEventDispatcher();

	import Markdown from './Markdown.svelte';
	import { chatId, mobile, showArtifacts, showControls, showOverview } from '$lib/stores';
	import { createMessagesList } from '$lib/utils';

	export let id;
	export let content;
	export let history;
	export let model = null;
	export let sources = null;

	export let save = false;

	export let onSourceClick = () => {};
	export let onAddMessages = () => {};

	let contentContainerElement;
</script>

<div bind:this={contentContainerElement}>
	<Markdown
		{id}
		{content}
		{model}
		{save}
		sourceIds={(sources ?? []).reduce((acc, s) => {
			let ids = [];
			s.document.forEach((document, index) => {
				const metadata = s.metadata?.[index];
				const id = metadata?.source ?? 'N/A';

				if (metadata?.name) {
					ids.push(metadata.name);
					return ids;
				}

				if (id.startsWith('http://') || id.startsWith('https://')) {
					ids.push(id);
				} else {
					ids.push(s?.source?.name ?? id);
				}

				return ids;
			});

			acc = [...acc, ...ids];

			// remove duplicates
			return acc.filter((item, index) => acc.indexOf(item) === index);
		}, [])}
		{onSourceClick}
		on:update={(e) => {
			dispatch('update', e.detail);
		}}
		on:code={(e) => {
			const { lang, code } = e.detail;

			if (
				(['html', 'svg'].includes(lang) || (lang === 'xml' && code.includes('svg'))) &&
				!$mobile &&
				$chatId
			) {
				showArtifacts.set(true);
				showControls.set(true);
			}
		}}
	/>
</div>