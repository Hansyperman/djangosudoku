var sudokuApp=angular.module('sudokuApp',[]);
var dimension=3;
var dimension2=dimension*dimension;


sudokuApp.factory('selectedSymbolService', function() {
  return {selectedSymbol:'?'};
});

/* Controller for the symbol picker.
   
   It is responsible for magaing the selected symbol
 
 */
sudokuApp.controller('symbolsController',function symbolsController($scope,selectedSymbolService) {
  // Fill the grid with cells
  $scope.rows=[];
  var symbol=1;
  for(i=0;i<dimension;i++){
    var row={
      cells:[]
    };
    for(j=0;j<dimension;j++){
      row.cells.push({
	symbol:symbol
      });
      symbol++;
    }
    $scope.rows.push(row);

    $scope.emptyCell={symbol:'?'}

    
    //Select 1 cell
    $scope.selectedSymbol=selectedSymbolService.selectedSymbol;
    
    $scope.onSymbolClicked=function(cell){
     $scope.selectedSymbol=cell.symbol;
     selectedSymbolService.selectedSymbol=cell.symbol;
    }
  }
});


/* Controller for the main sudoku control 
 *  It is responsible for storing and editing the current sudoku, and for commmunicating with the back end
 */
sudokuApp.controller('sudokuController',function sudokuController($scope,selectedSymbolService) {
  $scope.rows=[];
  var symbol=1;
  for(i=0;i<dimension2;i++){
    var row={
      name:String.fromCharCode("A".charCodeAt(0)+i),
      cells:[]
    };
    for(j=0;j<dimension2;j++){
      var cell={
	symbol: symbol
      };
      row.cells.push(cell);
      symbol=(symbol%7)+1;
    }
    $scope.rows.push(row);
  }
   
   
  $scope.onCellClicked=function(cell){
      cell.symbol=selectedSymbolService.selectedSymbol;
    }
});