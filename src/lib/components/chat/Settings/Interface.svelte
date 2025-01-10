<script lang="ts">
	import { getBackendConfig } from '$lib/apis';
	import { setDefaultPromptSuggestions } from '$lib/apis/configs';
	import { config, models, settings, user } from '$lib/stores';
	import { createEventDispatcher, onMount, getContext } from 'svelte';
	import { toast } from 'svelte-sonner';
	import Tooltip from '$lib/components/common/Tooltip.svelte';
	import { updateUserInfo } from '$lib/apis/users';
	import { getUserPosition } from '$lib/utils';
	const dispatch = createEventDispatcher();

	const i18n = getContext('i18n');

	export let saveSettings: Function;

	let backgroundImageUrl = null;
	let inputFiles = null;
	let filesInputElement;

	// Addons
	let titleAutoGenerate = true;

	let responseAutoCopy = false;
	let widescreenMode = false;
	let splitLargeChunks = false;
	let scrollOnBranchChange = true;
	let userLocation = false;

	// Interface
	let defaultModelId = '';
	let showUsername = false;
	let richTextInput = true;
	let largeTextAsFile = false;
	let notificationSound = false;

	let landingPageMode = '';
	let chatBubble = true;
	let chatDirection: 'LTR' | 'RTL' = 'LTR';

	let imageCompression = false;
	let imageCompressionSize = {
		width: '',
		height: ''
	};

	// Admin - Show Update Available Toast
	let showUpdateToast = false;

	let showEmojiInCall = false;
	let voiceInterruption = false;
	let hapticFeedback = false;

	const togglesScrollOnBranchChange = async () => {
		scrollOnBranchChange = !scrollOnBranchChange;
		saveSettings({ scrollOnBranchChange: scrollOnBranchChange });
	};

	const toggleWidescreenMode = async () => {
		widescreenMode = !widescreenMode;
		saveSettings({ widescreenMode: widescreenMode });
	};

	const toggleChatBubble = async () => {
		chatBubble = !chatBubble;
		saveSettings({ chatBubble: chatBubble });
	};

	const toggleLandingPageMode = async () => {
		landingPageMode = landingPageMode === '' ? 'chat' : '';
		saveSettings({ landingPageMode: landingPageMode });
	};

	const toggleShowUsername = async () => {
		showUsername = !showUsername;
		saveSettings({ showUsername: showUsername });
	};

	const toggleTitleAutoGenerate = async () => {
		titleAutoGenerate = !titleAutoGenerate;
		saveSettings({
			title: {
				...$settings.title,
				auto: titleAutoGenerate
			}
		});
	};

	const toggleChangeChatDirection = async () => {
		chatDirection = chatDirection === 'LTR' ? 'RTL' : 'LTR';
		saveSettings({ chatDirection });
	};

	const updateInterfaceHandler = async () => {
		saveSettings({
			models: [defaultModelId],
			imageCompressionSize: imageCompressionSize
		});
	};

	onMount(async () => {
		titleAutoGenerate = $settings?.title?.auto ?? true;

		responseAutoCopy = $settings.responseAutoCopy ?? false;

		showUsername = $settings.showUsername ?? false;
		showUpdateToast = false;

		showEmojiInCall = false;
		voiceInterruption = false;

		richTextInput = false;
		largeTextAsFile = false;

		landingPageMode = $settings.landingPageMode ?? '';
		chatBubble = $settings.chatBubble ?? true;
		widescreenMode = $settings.widescreenMode ?? false;
		splitLargeChunks = $settings.splitLargeChunks ?? false;
		scrollOnBranchChange = $settings.scrollOnBranchChange ?? true;
		chatDirection = $settings.chatDirection ?? 'LTR';
		userLocation = $settings.userLocation ?? false;

		notificationSound = false;

		hapticFeedback = false;

		imageCompression = $settings.imageCompression ?? false;
		imageCompressionSize = $settings.imageCompressionSize ?? { width: '', height: '' };

		defaultModelId = $settings?.models?.at(0) ?? '';
		if ($config?.default_models) {
			defaultModelId = $config.default_models.split(',')[0];
		}

		backgroundImageUrl = $settings.backgroundImageUrl ?? null;
	});
</script>

<form
	class="flex flex-col h-full justify-between space-y-3 text-sm"
	on:submit|preventDefault={() => {
		updateInterfaceHandler();
		dispatch('save');
	}}
>
	<input
		bind:this={filesInputElement}
		bind:files={inputFiles}
		type="file"
		hidden
		accept="image/*"
		on:change={() => {
			let reader = new FileReader();
			reader.onload = (event) => {
				let originalImageUrl = `${event.target.result}`;

				backgroundImageUrl = originalImageUrl;
				saveSettings({ backgroundImageUrl });
			};

			if (
				inputFiles &&
				inputFiles.length > 0 &&
				['image/gif', 'image/webp', 'image/jpeg', 'image/png'].includes(inputFiles[0]['type'])
			) {
				reader.readAsDataURL(inputFiles[0]);
			} else {
				console.log(`Unsupported File Type '${inputFiles[0]['type']}'.`);
				inputFiles = null;
			}
		}}
	/>

	<div class=" space-y-3 overflow-y-scroll max-h-[28rem] lg:max-h-full">
		<div>
			<div class=" mb-1.5 text-sm font-medium">{$i18n.t('UI')}</div>

			<div>
				<div class=" py-0.5 flex w-full justify-between">
					<div class=" self-center text-xs">{$i18n.t('Landing Page Mode')}</div>

					<button
						class="p-1 px-3 text-xs flex rounded transition"
						on:click={() => {
							toggleLandingPageMode();
						}}
						type="button"
					>
						{#if landingPageMode === ''}
							<span class="ml-2 self-center">{$i18n.t('Default')}</span>
						{:else}
							<span class="ml-2 self-center">{$i18n.t('Chat')}</span>
						{/if}
					</button>
				</div>
			</div>

			<div>
				<div class=" py-0.5 flex w-full justify-between">
					<div class=" self-center text-xs">{$i18n.t('Chat Bubble UI')}</div>

					<button
						class="p-1 px-3 text-xs flex rounded transition"
						on:click={() => {
							toggleChatBubble();
						}}
						type="button"
					>
						{#if chatBubble === true}
							<span class="ml-2 self-center">{$i18n.t('On')}</span>
						{:else}
							<span class="ml-2 self-center">{$i18n.t('Off')}</span>
						{/if}
					</button>
				</div>
			</div>

			{#if !$settings.chatBubble}
				<div>
					<div class=" py-0.5 flex w-full justify-between">
						<div class=" self-center text-xs">
							{$i18n.t('Display the username instead of You in the Chat')}
						</div>

						<button
							class="p-1 px-3 text-xs flex rounded transition"
							on:click={() => {
								toggleShowUsername();
							}}
							type="button"
						>
							{#if showUsername === true}
								<span class="ml-2 self-center">{$i18n.t('On')}</span>
							{:else}
								<span class="ml-2 self-center">{$i18n.t('Off')}</span>
							{/if}
						</button>
					</div>
				</div>
			{/if}

			<div>
				<div class=" py-0.5 flex w-full justify-between">
					<div class=" self-center text-xs">{$i18n.t('Widescreen Mode')}</div>

					<button
						class="p-1 px-3 text-xs flex rounded transition"
						on:click={() => {
							toggleWidescreenMode();
						}}
						type="button"
					>
						{#if widescreenMode === true}
							<span class="ml-2 self-center">{$i18n.t('On')}</span>
						{:else}
							<span class="ml-2 self-center">{$i18n.t('Off')}</span>
						{/if}
					</button>
				</div>
			</div>

			<div>
				<div class=" py-0.5 flex w-full justify-between">
					<div class=" self-center text-xs">{$i18n.t('Chat direction')}</div>

					<button
						class="p-1 px-3 text-xs flex rounded transition"
						on:click={toggleChangeChatDirection}
						type="button"
					>
						{#if chatDirection === 'LTR'}
							<span class="ml-2 self-center">{$i18n.t('LTR')}</span>
						{:else}
							<span class="ml-2 self-center">{$i18n.t('RTL')}</span>
						{/if}
					</button>
				</div>
			</div>

			<div class=" my-1.5 text-sm font-medium">{$i18n.t('Chat')}</div>

			<div>
				<div class=" py-0.5 flex w-full justify-between">
					<div class=" self-center text-xs">{$i18n.t('Title Auto-Generation')}</div>

					<button
						class="p-1 px-3 text-xs flex rounded transition"
						on:click={() => {
							toggleTitleAutoGenerate();
						}}
						type="button"
					>
						{#if titleAutoGenerate === true}
							<span class="ml-2 self-center">{$i18n.t('On')}</span>
						{:else}
							<span class="ml-2 self-center">{$i18n.t('Off')}</span>
						{/if}
					</button>
				</div>
			</div>

			<div>
				<div class=" py-0.5 flex w-full justify-between">
					<div class=" self-center text-xs">
						{$i18n.t('Chat Background Image')}
					</div>

					<button
						class="p-1 px-3 text-xs flex rounded transition"
						on:click={() => {
							if (backgroundImageUrl !== null) {
								backgroundImageUrl = null;
								saveSettings({ backgroundImageUrl });
							} else {
								filesInputElement.click();
							}
						}}
						type="button"
					>
						{#if backgroundImageUrl !== null}
							<span class="ml-2 self-center">{$i18n.t('Reset')}</span>
						{:else}
							<span class="ml-2 self-center">{$i18n.t('Upload')}</span>
						{/if}
					</button>
				</div>
			</div>

			<!-- <div>
				<div class=" py-0.5 flex w-full justify-between">
					<div class=" self-center text-xs">
						{$i18n.t('Fluidly stream large external response chunks')}
					</div>

					<button
						class="p-1 px-3 text-xs flex rounded transition"
						on:click={() => {
							toggleSplitLargeChunks();
						}}
						type="button"
					>
						{#if splitLargeChunks === true}
							<span class="ml-2 self-center">{$i18n.t('On')}</span>
						{:else}
							<span class="ml-2 self-center">{$i18n.t('Off')}</span>
						{/if}
					</button>
				</div>
			</div> -->

			<div>
				<div class=" py-0.5 flex w-full justify-between">
					<div class=" self-center text-xs">
						{$i18n.t('Scroll to bottom when switching between branches')}
					</div>

					<button
						class="p-1 px-3 text-xs flex rounded transition"
						on:click={() => {
							togglesScrollOnBranchChange();
						}}
						type="button"
					>
						{#if scrollOnBranchChange === true}
							<span class="ml-2 self-center">{$i18n.t('On')}</span>
						{:else}
							<span class="ml-2 self-center">{$i18n.t('Off')}</span>
						{/if}
					</button>
				</div>
			</div>

		</div>
	</div>

	<div class="flex justify-end text-sm font-medium">
		<button
			class="px-3.5 py-1.5 text-sm font-medium bg-black hover:bg-gray-900 text-white dark:bg-white dark:text-black dark:hover:bg-gray-100 transition rounded-full"
			type="submit"
		>
			{$i18n.t('Save')}
		</button>
	</div>
</form>
