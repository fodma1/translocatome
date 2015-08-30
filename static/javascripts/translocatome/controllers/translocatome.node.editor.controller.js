(function () {
    'use strict';

    angular
        .module('thinkster.translocatome.controllers')
        .controller('TranslocatomeNodeEditorController', TranslocatomeNodeEditorController);

    TranslocatomeNodeEditorController.$inject = ['$scope', '$http'];

    function TranslocatomeNodeEditorController($scope, $http) {

        function init()
        {
            $scope.displayText = 'This text should be displayed!';
        }

        init();
    }
})();
