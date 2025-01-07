<script lang="ts">
	import { getBackendConfig } from '$lib/apis';
	import {
		getAdminConfig,
		getLdapConfig,
		getLdapServer,
		updateAdminConfig,
		updateLdapConfig,
		updateLdapServer
	} from '$lib/apis/auths';
	import SensitiveInput from '$lib/components/common/SensitiveInput.svelte';
	import Switch from '$lib/components/common/Switch.svelte';
	import Tooltip from '$lib/components/common/Tooltip.svelte';
	import { config } from '$lib/stores';
	import { onMount, getContext } from 'svelte';
	import { toast } from 'svelte-sonner';

	const i18n = getContext('i18n');

	export let saveHandler: Function;

	let adminConfig = null;

	// LDAP
	let ENABLE_LDAP = false;
	let LDAP_SERVER = {
		label: '',
		host: '',
		port: '',
		attribute_for_username: 'uid',
		app_dn: '',
		app_dn_password: '',
		search_base: '',
		search_filters: '',
		use_tls: false,
		certificate_path: '',
		ciphers: ''
	};

	const updateLdapServerHandler = async () => {
		if (!ENABLE_LDAP) return;
		const res = await updateLdapServer(localStorage.token, LDAP_SERVER).catch((error) => {
			toast.error(error);
			return null;
		});
		if (res) {
			toast.success($i18n.t('LDAP server updated'));
		}
	};

	const updateHandler = async () => {
		const res = await updateAdminConfig(localStorage.token, adminConfig);
		await updateLdapServerHandler();

		if (res) {
			saveHandler();
		} else {
			toast.error(i18n.t('Failed to update settings'));
		}
	};

	onMount(async () => {
		await Promise.all([
			(async () => {
				adminConfig = await getAdminConfig(localStorage.token);
			})(),
			(async () => {
				LDAP_SERVER = await getLdapServer(localStorage.token);
			})()
		]);

		const ldapConfig = await getLdapConfig(localStorage.token);
		ENABLE_LDAP = ldapConfig.ENABLE_LDAP;
	});
</script>

<form
	class="flex flex-col h-full justify-between space-y-3 text-sm"
	on:submit|preventDefault={async () => {
		updateHandler();
	}}
>
	<div class=" space-y-3 overflow-y-scroll scrollbar-hidden h-full">
		{#if adminConfig !== null}
			<div>
				<div class=" mb-3 text-sm font-medium">{$i18n.t('General Settings')}</div>

				<div class="  flex w-full justify-between pr-2">
					<div class=" self-center text-xs font-medium">{$i18n.t('Enable New Sign Ups')}</div>

					<Switch bind:state={adminConfig.ENABLE_SIGNUP} />
				</div>

				<div class="  my-3 flex w-full justify-between">
					<div class=" self-center text-xs font-medium">{$i18n.t('Default User Role')}</div>
					<div class="flex items-center relative">
						<select
							class="dark:bg-gray-900 w-fit pr-8 rounded px-2 text-xs bg-transparent outline-none text-right"
							bind:value={adminConfig.DEFAULT_USER_ROLE}
							placeholder="Select a role"
						>
							<option value="pending">{$i18n.t('pending')}</option>
							<option value="user">{$i18n.t('user')}</option>
							<option value="admin">{$i18n.t('admin')}</option>
						</select>
					</div>
				</div>

				<div class=" flex w-full justify-between pr-2 my-3">
					<div class=" self-center text-xs font-medium">{$i18n.t('Enable API Key')}</div>

					<Switch bind:state={adminConfig.ENABLE_API_KEY} />
				</div>

				{#if adminConfig?.ENABLE_API_KEY}
					<div class=" flex w-full justify-between pr-2 my-3">
						<div class=" self-center text-xs font-medium">
							{$i18n.t('API Key Endpoint Restrictions')}
						</div>

						<Switch bind:state={adminConfig.ENABLE_API_KEY_ENDPOINT_RESTRICTIONS} />
					</div>

					{#if adminConfig?.ENABLE_API_KEY_ENDPOINT_RESTRICTIONS}
						<div class=" flex w-full flex-col pr-2">
							<div class=" text-xs font-medium">
								{$i18n.t('Allowed Endpoints')}
							</div>

							<input
								class="w-full mt-1 rounded-lg text-sm dark:text-gray-300 bg-transparent outline-none"
								type="text"
								placeholder={`e.g.) /api/v1/messages, /api/v1/channels`}
								bind:value={adminConfig.API_KEY_ALLOWED_ENDPOINTS}
							/>

							<div class="mt-2 text-xs text-gray-400 dark:text-gray-500">
								<!-- https://docs.openwebui.com/getting-started/advanced-topics/api-endpoints -->
								<a
									href="https://docs.openwebui.com/getting-started/advanced-topics/api-endpoints"
									target="_blank"
									class=" text-gray-300 font-medium underline"
								>
									{$i18n.t('To learn more about available endpoints, visit our documentation.')}
								</a>
							</div>
						</div>
					{/if}
				{/if}

				<hr class=" border-gray-50 dark:border-gray-850 my-2" />

				<div class=" w-full justify-between">
					<div class="flex w-full justify-between">
						<div class=" self-center text-xs font-medium">{$i18n.t('WebUI URL')}</div>
					</div>

					<div class="flex mt-2 space-x-2">
						<input
							class="w-full rounded-lg py-2 px-4 text-sm bg-gray-50 dark:text-gray-300 dark:bg-gray-850 outline-none"
							type="text"
							placeholder={`e.g.) "http://localhost:3000"`}
							bind:value={adminConfig.WEBUI_URL}
						/>
					</div>

					<div class="mt-2 text-xs text-gray-400 dark:text-gray-500">
						{$i18n.t(
							'Enter the public URL of your WebUI. This URL will be used to generate links in the notifications.'
						)}
					</div>
				</div>
			</div>
		{/if}
	</div>

	<div class="flex justify-end pt-3 text-sm font-medium">
		<button
			class="px-3.5 py-1.5 text-sm font-medium bg-black hover:bg-gray-900 text-white dark:bg-white dark:text-black dark:hover:bg-gray-100 transition rounded-full"
			type="submit"
		>
			{$i18n.t('Save')}
		</button>
	</div>
</form>
