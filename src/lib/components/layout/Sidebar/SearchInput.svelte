<script lang="ts">
	import { getContext, createEventDispatcher, onMount, onDestroy, tick } from 'svelte';
	import { fade } from 'svelte/transition';

	const dispatch = createEventDispatcher();
	const i18n = getContext('i18n');

	export let placeholder = '';
	export let value = '';

	let selectedIdx = 0;

	let lastWord = '';
	$: lastWord = value ? value.split(' ').at(-1) : value;

	const documentClickHandler = (e) => {
		const searchContainer = document.getElementById('search-container');
		const chatSearch = document.getElementById('chat-search');

		if (!searchContainer.contains(e.target) && !chatSearch.contains(e.target)) {
			if (e.target.id.startsWith('search-tag-') || e.target.id.startsWith('search-option-')) {
				return;
			}
		}
	};

	onMount(() => {
		document.addEventListener('click', documentClickHandler);
	});

	onDestroy(() => {
		document.removeEventListener('click', documentClickHandler);
	});
</script>

<div class="px-1 mb-1 flex justify-center space-x-2 relative z-10" id="search-container">
	<div class="flex w-full rounded-xl" id="chat-search">
		<div class="self-center pl-3 py-2 rounded-l-xl bg-transparent">
			<svg
				xmlns="http://www.w3.org/2000/svg"
				viewBox="0 0 20 20"
				fill="currentColor"
				class="w-4 h-4"
			>
				<path
					fill-rule="evenodd"
					d="M9 3.5a5.5 5.5 0 100 11 5.5 5.5 0 000-11zM2 9a7 7 0 1112.452 4.391l3.328 3.329a.75.75 0 11-1.06 1.06l-3.329-3.328A7 7 0 012 9z"
					clip-rule="evenodd"
				/>
			</svg>
		</div>

		<input
			class="w-full rounded-r-xl py-1.5 pl-2.5 pr-4 text-sm bg-transparent dark:text-gray-300 outline-none"
			placeholder={placeholder ? placeholder : $i18n.t('Search')}
			bind:value
			on:input={() => {
				dispatch('input');
			}}
			on:keydown={(e) => {
				if (e.key === 'ArrowUp') {
					e.preventDefault();
					selectedIdx = Math.max(0, selectedIdx - 1);
				} else if (e.key === 'ArrowDown') {
					e.preventDefault();
				} else {
					// if the user types something, reset to the top selection.
					selectedIdx = 0;
				}
			}}
		/>
	</div>
</div>
