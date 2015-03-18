var app = angular.module('school',[]);

app.controller('StudentCtrl', ['$scope', '$http', function($scope, $http){
    var apiurl = '/api/student';
    $scope.objectList = [];
    $scope.form={
        item:{}
    };

    $http.get(apiurl).success(function(response){
        $scope.objectList = response.objects;
    });

    $scope.add = function(){
        $http.post(apiurl, $scope.form.item).success(function(response){
            $scope.objectList.push(response);
            $scope.form.item={};
        });
    }
}]);