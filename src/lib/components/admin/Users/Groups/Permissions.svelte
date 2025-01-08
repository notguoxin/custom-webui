<script lang="ts">
	import { getContext } from 'svelte';
	const i18n = getContext('i18n');

	import Switch from '$lib/components/common/Switch.svelte';
	import Tooltip from '$lib/components/common/Tooltip.svelte';

	export let permissions = {
		workspace: {
			models: false
		},
		chat: {
			delete: true,
			edit: true,
			temporary: true,
			file_upload: true
		}
	};
</script>

<div>
	<div>
		<div class=" mb-2 text-sm font-medium">{$i18n.t('Workspace Permissions')}</div>

		<div class="  flex w-full justify-between my-2 pr-2">
			<div class=" self-center text-xs font-medium">
				{$i18n.t('Models Access')}
			</div>
			<Switch bind:state={permissions.workspace.models} />
		</div>

		<hr class=" border-gray-50 dark:border-gray-850 my-2" />

		<div>
			<div class=" mb-2 text-sm font-medium">{$i18n.t('Chat Permissions')}</div>

			<div class="  flex w-full justify-between my-2 pr-2">
				<div class=" self-center text-xs font-medium">
					{$i18n.t('Allow File Upload')}
				</div>

				<Switch bind:state={permissions.chat.file_upload} />
			</div>

			<div class="  flex w-full justify-between my-2 pr-2">
				<div class=" self-center text-xs font-medium">
					{$i18n.t('Allow Chat Delete')}
				</div>

				<Switch bind:state={permissions.chat.delete} />
			</div>

			<div class="  flex w-full justify-between my-2 pr-2">
				<div class=" self-center text-xs font-medium">
					{$i18n.t('Allow Chat Edit')}
				</div>

				<Switch bind:state={permissions.chat.edit} />
			</div>

			<div class="  flex w-full justify-between my-2 pr-2">
				<div class=" self-center text-xs font-medium">
					{$i18n.t('Allow Temporary Chat')}
				</div>

				<Switch bind:state={permissions.chat.temporary} />
			</div>
		</div>
	</div>
</div>
