var app = angular.module('myApp', []).config(function ($interpolateProvider) {
        $interpolateProvider.startSymbol('{[{').endSymbol('}]}');
        });

app.controller('LoginCtrl', function ($scope, $rootScope, $http) {

var tokentype = 'Bearer';
var access_token = '3WNlMtDK1KUvwn7tx3JlIMYcZTHulQ'

$scope.ShowAllStudents = function(){
        $http({
            method: "GET",
            url: 'http://127.0.0.1:8181/GetAllStudents/',
            headers: { 'Authorization': tokentype + ' ' + access_token },
        }).success(function (response) {
            $scope.UserList = response           

        }).error(function (error) {
            alert("err: " + error);            
        })
        }

       $scope.ShowAllStudents();        
       });
