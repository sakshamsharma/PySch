var scroll=angular.module('PySch', []);


scroll.controller('mainRaj', function($scope, $http) {
	$scope.items = []
	$scope.author = ""
	$scope.authorcites = ""
	$scope.authorh = ""
	$scope.authori = ""
	$scope.category = "author"
	$scope.sorti = "cites"
	$scope.loading = false

	$scope.urlGen = function(inputstr) {
		return 'http://localhost:8000/server/' + $scope.category + '/1?author=' + inputstr
	}

	$scope.checkKey = function(keyEvent) {
		if (keyEvent.which === 13) {
			$scope.loading = true;
			inputstr = keyEvent.target.value;
			url = $scope.urlGen(inputstr);
			val = $http.get(url);
			val.success(function(res) {
				var data = JSON.parse(res);
				$scope.items = data.papers;
				$scope.author = data.name;
				$scope.authorcites = data.cites;
				$scope.authorh = data.hindex;
				$scope.authori = data.iindex;
				$scope.loading = false;
			})
		};
	}

	$scope.sorter = function() {
		if($scope.sorti == "cites") {
			$scope.items.sort(function(a,b) {
				return a.cites - b.cites;
			})
		} else if($scope.sorti == "year") {
			$scope.items.sort(function(a,b) {
				return b.year - a.year;
			})
		}
	}

	$scope.cate = function(cate) {
		$scope.category = cate;
	}

})
