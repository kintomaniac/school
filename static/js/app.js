var app = angular.module('school',[]);

app.controller('StudentCtrl', ['$scope', '$http', function($scope, $http){
    var apiurl = '/api/student';
    $scope.objectList = [];
    $scope.standardList=['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X'];
    $scope.form={
        item:{}
    };
    $scope.filterForm={};

    //Filter
    var q={
        filters:[]
    };

    //Get Student list
    $scope.getStudents = function() {
        if($scope.filterForm.standard){
            q.filters = [{
                name : "student_standard",
                op : "==",
                val : $scope.filterForm.standard
            }];
        }
        $http.get(apiurl + '?q=' + JSON.stringify(q)).success(function (response) {
            $scope.objectList = response.objects;
        });
    }

    //Add new student
    $scope.add = function(){
        $http.post(apiurl, $scope.form.item).success(function(response){
            $scope.objectList.push(response);
            $scope.form.item={};
        });
    }

    $scope.getStudents();
}]);