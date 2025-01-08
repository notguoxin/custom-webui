<script>
    import { toast } from 'svelte-sonner';

    import { onMount, getContext } from 'svelte';
    import { goto } from '$app/navigation';
    import { page } from '$app/stores';

    import { getBackendConfig } from '$lib/apis';
    import { getSessionUser, userSignIn, userSignUp } from '$lib/apis/auths';

    import { WEBUI_API_BASE_URL, WEBUI_BASE_URL } from '$lib/constants';
    import { WEBUI_NAME, config, user, socket } from '$lib/stores';

    import { generateInitialsImage, canvasPixelTest } from '$lib/utils';

    import Spinner from '$lib/components/common/Spinner.svelte';
    import OnBoarding from '$lib/components/OnBoarding.svelte';

    const i18n = getContext('i18n');

    let loaded = false;

    let mode = 'signin';

    let name = '';
    let email = '';
    let password = '';

	const setSessionUser = async (sessionUser) => {
		if (sessionUser) {
            console.log(sessionUser);
            toast.success($i18n.t(`You're now logged in.`));
            if (sessionUser.token) {
                localStorage.token = sessionUser.token;
            }

            $socket.emit('user-join', { auth: { token: sessionUser.token } });
            await user.set(sessionUser);
            await config.set(await getBackendConfig());
            goto('/');
        }
    };

    const signInHandler = async () => {
        const sessionUser = await userSignIn(email, password).catch((error) => {
            toast.error(error);
            return null;
        });

        await setSessionUser(sessionUser);
    };

    const signUpHandler = async () => {
        const sessionUser = await userSignUp(name, email, password, generateInitialsImage(name)).catch(
            (error) => {
                toast.error(error);
                return null;
            }
        );

        await setSessionUser(sessionUser);
    };

    const submitHandler = async () => {
        if (mode === 'signin') {
            await signInHandler();
        } else {
            await signUpHandler();
        }
    };

    let onboarding = false;

    onMount(async () => {
        if ($user !== undefined) {
            await goto('/');
        }

        loaded = true;
        if ($config?.features.auth === false) {
            await signInHandler();
        } else {
            onboarding = $config?.onboarding ?? false;
        }
    });
</script>

<svelte:head>
    <title>
        {`${$WEBUI_NAME}`}
    </title>
</svelte:head>

<OnBoarding
    bind:show={onboarding}
    getStartedHandler={() => {
        onboarding = false;
        mode = 'signup';
    }}
/>

<div class="w-full h-screen max-h-[100dvh] text-white relative">
    <div class="w-full h-full absolute top-0 left-0 bg-white dark:bg-black"></div>

    {#if loaded}
        <div class="fixed m-10 z-50">
            <div class="flex space-x-2">
                <div class=" self-center">
                    <img
                        crossorigin="anonymous"
                        src="{WEBUI_BASE_URL}/static/favicon.png"
                        class=" w-6 rounded-full"
                        alt="logo"
                    />
                </div>
            </div>
        </div>

        <div
            class="fixed bg-transparent min-h-screen w-full flex justify-center font-primary z-50 text-black dark:text-white"
        >
            <div class="w-full sm:max-w-md px-10 min-h-screen flex flex-col text-center">
                {#if $config?.features.auth === false}
                    <div class=" my-auto pb-10 w-full">
                        <div
                            class="flex items-center justify-center gap-3 text-xl sm:text-2xl text-center font-semibold dark:text-gray-200"
                        >
                            <div>
                                {$i18n.t('Signing in to {{WEBUI_NAME}}', { WEBUI_NAME: $WEBUI_NAME })}
                            </div>

                            <div>
                                <Spinner />
                            </div>
                        </div>
                    </div>
                {:else}
                    <div class="  my-auto pb-10 w-full dark:text-gray-100">
                        <form
                            class=" flex flex-col justify-center"
                            on:submit={(e) => {
                                e.preventDefault();
                                submitHandler();
                            }}
                        >
                            <div class="mb-1">
                                <div class=" text-2xl font-medium">
                                    {#if $config?.onboarding ?? false}
                                        {$i18n.t(`Get started with {{WEBUI_NAME}}`, { WEBUI_NAME: $WEBUI_NAME })}
                                    {:else if mode === 'signin'}
                                        {$i18n.t(`Sign in to {{WEBUI_NAME}}`, { WEBUI_NAME: $WEBUI_NAME })}
                                    {:else}
                                        {$i18n.t(`Sign up to {{WEBUI_NAME}}`, { WEBUI_NAME: $WEBUI_NAME })}
                                    {/if}
                                </div>

                                {#if $config?.onboarding ?? false}
                                    <div class=" mt-1 text-xs font-medium text-gray-500">
                                        ⓘ {$WEBUI_NAME}
                                        {$i18n.t(
                                            'does not make any external connections, and your data stays securely on your locally hosted server.'
                                        )}
                                    </div>
                                {/if}
                            </div>

                            {#if $config?.features.enable_login_form}
                                <div class="flex flex-col mt-4">
                                    {#if mode === 'signup'}
                                        <div class="mb-2">
                                            <div class=" text-sm font-medium text-left mb-1">{$i18n.t('Name')}</div>
                                            <input
                                                bind:value={name}
                                                type="text"
                                                class="my-0.5 w-full text-sm outline-none bg-transparent"
                                                autocomplete="name"
                                                placeholder={$i18n.t('Enter Your Full Name')}
                                                required
                                            />
                                        </div>
                                    {/if}

                                    <div class="mb-2">
                                        <div class=" text-sm font-medium text-left mb-1">{$i18n.t('Email')}</div>
                                        <input
                                            bind:value={email}
                                            type="email"
                                            class="my-0.5 w-full text-sm outline-none bg-transparent"
                                            autocomplete="email"
                                            name="email"
                                            placeholder={$i18n.t('Enter Your Email')}
                                            required
                                        />
                                    </div>

                                    <div>
                                        <div class=" text-sm font-medium text-left mb-1">{$i18n.t('Password')}</div>

                                        <input
                                            bind:value={password}
                                            type="password"
                                            class="my-0.5 w-full text-sm outline-none bg-transparent"
                                            placeholder={$i18n.t('Enter Your Password')}
                                            autocomplete="current-password"
                                            name="current-password"
                                            required
                                        />
                                    </div>
                                </div>
                            {/if}
                            <div class="mt-5">
                                {#if $config?.features.enable_login_form}
                                    <button
                                        class="bg-gray-700/5 hover:bg-gray-700/10 dark:bg-gray-100/5 dark:hover:bg-gray-100/10 dark:text-gray-300 dark:hover:text-white transition w-full rounded-full font-medium text-sm py-2.5"
                                        type="submit"
                                    >
                                        {mode === 'signin'
                                            ? $i18n.t('Sign in')
                                            : ($config?.onboarding ?? false)
                                                ? $i18n.t('Create Admin Account')
                                                : $i18n.t('Create Account')}
                                    </button>

                                    {#if $config?.features.enable_signup && !($config?.onboarding ?? false)}
                                        <div class=" mt-4 text-sm text-center">
                                            {mode === 'signin'
                                                ? $i18n.t("Don't have an account?")
                                                : $i18n.t('Already have an account?')}

                                            <button
                                                class=" font-medium underline"
                                                type="button"
                                                on:click={() => {
                                                    if (mode === 'signin') {
                                                        mode = 'signup';
                                                    } else {
                                                        mode = 'signin';
                                                    }
                                                }}
                                            >
                                                {mode === 'signin' ? $i18n.t('Sign up') : $i18n.t('Sign in')}
                                            </button>
                                        </div>
                                    {/if}
                                {/if}
                            </div>
                        </form>
                    </div>
                {/if}
            </div>
        </div>
    {/if}
</div>