var scroll=angular.module('PySch', []);

scroll.controller('mainRaj', function($scope, $http) {
	$scope.items = []
	$scope.author = ""

	$scope.checkKey = function(keyEvent) {
		if (keyEvent.which === 13) {
			inputstr = keyEvent.target.value;
			val = $http.get('http://localhost:8000/server/author/1?author=' + inputstr);
			val.success(function(res) {
				var data = JSON.parse(res);
				$scope.items = data.papers;
				$scope.author = data.name;
			})
		};
	}

})
