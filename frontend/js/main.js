var scroll=angular.module('PySch', []);

scroll.controller('mainRaj', function($scope, $http) {
	$scope.items = []
	$scope.items_back = []
	$scope.author = ""
	$scope.authorcites = ""
	$scope.authorh = ""
	$scope.authori = ""
	$scope.category = "author"
	$scope.sorti = "cites"
	$scope.loading = false
	$scope.start_year = "1800"
	$scope.end_year = "2020"

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

	$scope.filterer = function() {
		$scope.items_back = $scope.items;
		//$scope.items.filter(function(el) {
			//return el.year <= $scope.end_year && el.year >= $scope.start_year;
		//})
		//console.log($scope.items);
		lister = [];
		console.log($scope.items);
		for(var t in $scope.items) {
			console.log($scope.items[t]);
			if($scope.items[ t ].year <= +$scope.end_year && $scope.items[ t ].year >= +$scope.start_year) {
				lister.push($scope.items[ t ]);
			}
		}
		$scope.items = lister;
		$scope.sorter();
	}

	$scope.cate = function(cate) {
		$scope.category = cate;
	}

})
