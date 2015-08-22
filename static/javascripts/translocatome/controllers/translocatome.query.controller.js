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

            $scope.sourceNode = {uni_prot_ac: '', gene_name: ''};
            $scope.targetNode = {uni_prot_ac: '', gene_name: ''};
            $scope.selectedInteraction = undefined;
        }

        $scope.queryNodesByUniProtAc = function(uniProtAc) {
            return $http.get('api/translocatome/query-nodes/', {
                params: {
                    uni_prot_ac: uniProtAc
                }
            }).then(function(response) {
                return response.data.nodes;
            });
        };

        $scope.onSourceSelect = function($item) {
            $scope.sourceNode.uni_prot_ac = $item.uni_prot_ac;
            $scope.sourceNode.gene_name = $item.gene_name;
        };

        $scope.onTargetSelect = function($item) {
            $scope.targetNode.uni_prot_ac = $item.uni_prot_ac;
            $scope.targetNode.gene_name = $item.gene_name;
        };

        init();
    }
})();
