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
            return $http.get('api/translocatome/query-nodes/', {
                params: {
                    uni_prot_ac: uniProtAc
                }
            }).then(function(response) {
                return response.data.nodes;
            });
        };

        $scope.onSourceSelect = function($item, $model, $label) {
            $scope.source.node.uni_prot_ac = $item.uni_prot_ac;
            $scope.source.node.gene_name = $item.gene_name;
        };

        $scope.displayAsString = function(node) {
            if (node) {
                return 'UniProtAC: ' + node.uni_prot_ac + ' GeneName: ' + node.gene_name;
            }
        };

        init();
    }
})();
