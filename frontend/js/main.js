var scroll=angular.module('PySch', []);

scroll.controller('mainRaj', function($scope, $http) {
	$scope.items = []
	$scope.author = ""
	$scope.authorcites = ""
	$scope.authorh = ""
	$scope.authori = ""

	$scope.checkKey = function(keyEvent) {
		if (keyEvent.which === 13) {
			inputstr = keyEvent.target.value;
			val = $http.get('http://localhost:8000/server/author/1?author=' + inputstr);
			val.success(function(res) {
				var data = JSON.parse(res);
				$scope.items = data.papers;
				$scope.author = data.name;
				$scope.authorcites = data.cites;
				$scope.authorh = data.hindex;
				$scope.authori = data.iindex;
			})
		};
	}

})
