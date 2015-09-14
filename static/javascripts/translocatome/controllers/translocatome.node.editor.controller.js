(function ()
{
    'use strict';

    angular
        .module('thinkster.translocatome.controllers')
        .controller('TranslocatomeNodeEditorController', TranslocatomeNodeEditorController);

    TranslocatomeNodeEditorController.$inject = ['$scope', '$http', 'growl'];

    function TranslocatomeNodeEditorController($scope, $http, growl)
    {

        function init()
        {
            $scope.node = $scope.ngDialogData.node || {};
            $scope.loading = false;
        }

        $scope.deleteNode = function ()
        {
            $scope.loading = true;
            if (confirm('Are you sure you want to delete this node?'))
            {
                $http.delete('api/translocatome/rest-api/node/' + $scope.node.id + '/')
                    .then(function ()
                    {
                        growl.addSuccessMessage('successfully deleted');
                    }, function (response)
                    {
                        growl.addErrorMessage('Errors: ' + response.data);
                    })
                    .finally(function ()
                    {
                        $scope.loading = false;
                    });
            }
        };

        $scope.save = function ()
        {
            $scope.loading = true;
            if ($scope.node.id)
            {
                $http.put('api/translocatome/rest-api/node/' + $scope.node.id + '/', $scope.node)
                    .then(function ()
                    {
                        growl.addSuccessMessage('successfully updated');
                    }, function (response)
                    {
                        growl.addErrorMessage('Errors: ' + response.data);
                    })
                    .finally(function ()
                    {
                        $scope.loading = false;
                    });
            } else
            {
                $http.post('api/translocatome/rest-api/node/', $scope.node)
                    .then(function ()
                    {
                        growl.addSuccessMessage('successfully updated');
                    }, function (response)
                    {
                        growl.addErrorMessage('Errors: ' + response.data);
                    })
                    .finally(function ()
                    {
                        $scope.loading = false;
                    });
            }
        };

        init();
    }
})();
