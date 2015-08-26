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

            $scope.selectedInteraction = undefined;
            $scope.interactions_with_meta = [];

            $scope.loadingNodes = {};
            $scope.noResults = {};

            $scope.showColumnSorter = false;
            $scope.displayedInteractionColumns = [
                'A',
                'B',
                'C',
                'D',
                'E',
                'F'
            ];
            $scope.interactionColumns = [
                'A',
                'B',
                'C',
                'D',
                'E',
                'F',
                'G',
                'H',
                'I',
                'J',
                'K',
                'L',
                'M',
                'N',
                'O',
                'P',
                'Q',
                'R',
                'S',
                'T',
                'U',
                'V',
                'W',
                'X',
                'Y',
                'Z'
            ];
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

        $scope.queryNodesByGeneName = function(geneName) {
            return $http.get('api/translocatome/query-nodes/', {
                params: {
                    gene_name: geneName
                }
            }).then(function(response) {
                return response.data.nodes;
            });
        };

        $scope.onSourceSelect = function($item) {
            $scope.sourceNode = angular.copy($item);
        };

        $scope.onTargetSelect = function($item) {
            $scope.targetNode = angular.copy($item);
        };

        $scope.swapNodes = function() {
            var tempNode = $scope.sourceNode;
            $scope.sourceNode = $scope.targetNode;
            $scope.targetNode = tempNode;
        };

        $scope.fetchInteractionsWithMeta = function() {
            var params = {};

            if ($scope.sourceNode) {
                params.source_node_id = $scope.sourceNode.id;
            }

            if ($scope.targetNode) {
                params.target_node_id = $scope.targetNode.id;
            }

            $http.get('api/translocatome/query-interactions/', {
                params: params
            }).then(function(response) {
                $scope.interactions_with_meta  = response.data.interactions;
            });
        };

        init();
    }
})();
