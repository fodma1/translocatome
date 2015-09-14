(function ()
{
    'use strict';

    angular
        .module('thinkster.routes')
        .config(config);

    //config.$inject = ['$routeProvider'];
    config.$inject = ['$stateProvider', '$urlRouterProvider'];

    /**
     * @name config
     * @desc Define valid application routes
     */
    //function config($routeProvider) {
    function config($stateProvider, $urlRouterProvider)
    {

        // For any unmatched URL
        $urlRouterProvider.otherwise('/');

        // States
        $stateProvider
            .state('index', {
                url: '/',
                controller: 'IndexController',
                controllerAs: 'vm',
                templateUrl: '/static/templates/layout/index.html'
            })
            .state('register', {
                url: '/register',
                controller: 'IndexController',
                controllerAs: 'vm',
                templateUrl: '/static/templates/layout/index.html'
            })
            .state('login', {
                url: '/login',
                controller: 'LoginController',
                controllerAs: 'vm',
                templateUrl: '/static/templates/authentication/login.html'
            })
            .state('interaction_list', {
                url: '/translocatome/interaction',
                controller: 'TranslocatomeInteractionController',
                templateUrl: '/static/templates/translocatome/interaction.html'
            })
            .state('node_list', {
                url: '/translocatome/node',
                controller: 'TranslocatomeNodeController',
                templateUrl: '/static/templates/translocatome/node.html'
            })
            .state('user', {
                url: '/+:username',
                controller: 'AccountController',
                controllerAs: 'vm',
                templateUrl: '/static/templates/accounts/account.html'
            })
            .state('user_settings', {
                url: '/+:username/settings',
                controller: 'AccountSettingsController',
                controllerAs: 'vm',
                templateUrl: '/static/templates/accounts/settings.html'
            });
    }
})();
