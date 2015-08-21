(function () {
    'use strict';

    angular
        .module('thinkster.translocatome.controllers')
        .controller('TranslocatomeQueryController', TranslocatomeQueryController);

    TranslocatomeQueryController.$inject = ['$scope', '$http'];

    function TranslocatomeQueryController($scope, $http) {

        function init() {
            $scope.source_nodes = [];
            $scope.target_nodes = [];
        }

        $scope.queryNodesByUniProtAc = function(uniProtAc) {
            return $http.get('api/translocatome/api/query-nodes', {
                params: {
                    uni_prot_ac: uniProtAc
                }
            }).then(function(response) {
                return response.data.nodes;
            });
        };

        init();
    }
})();