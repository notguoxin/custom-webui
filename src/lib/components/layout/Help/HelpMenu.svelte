<script lang="ts">
	import { DropdownMenu } from 'bits-ui';
	import { getContext } from 'svelte';

	import { showSettings } from '$lib/stores';
	import { flyAndScale } from '$lib/utils/transitions';

	import Dropdown from '$lib/components/common/Dropdown.svelte';
	import QuestionMarkCircle from '$lib/components/icons/QuestionMarkCircle.svelte';
	import Lifebuoy from '$lib/components/icons/Lifebuoy.svelte';
	import Keyboard from '$lib/components/icons/Keyboard.svelte';
	const i18n = getContext('i18n');

	export let showDocsHandler: Function;
	export let showShortcutsHandler: Function;

	export let onClose: Function = () => {};
</script>

<Dropdown
	on:change={(e) => {
		if (e.detail === false) {
			onClose();
		}
	}}
>
	<slot />

	<div slot="content">
	</div>
</Dropdown>
