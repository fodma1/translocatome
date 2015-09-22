(function ()
{
    'use strict';

    angular
        .module('thinkster', [
            'thinkster.config',
            'thinkster.routes',
            'thinkster.accounts',
            'thinkster.authentication',
            'thinkster.layout',
            'thinkster.posts',
            'thinkster.translocatome',
            'thinkster.utils',
            'angular-growl'
        ]);

    angular
        .module('thinkster.config', []);

    angular
        .module('thinkster.routes', ['ngRoute', 'ui.router']);

    angular
        .module('thinkster')
        .run(run);

    run.$inject = ['$http', 'formlyConfig'];
    function run($http, formlyConfig)
    {
        $http.defaults.xsrfHeaderName = 'X-CSRFToken';
        $http.defaults.xsrfCookieName = 'csrftoken';
        formlyConfig.setType({
            name:'tag',
            template:"<label class='control-label' ng-if='to.label'>{{to.label}}</label>" +
            "<tags-input ng-model='model[options.key]' ng-attr-placeholder='{{to.placeholder}}'>" +
            "<auto-complete source='{{to.tags}}'></auto-complete></tags-input>"
        });
    }
})();
