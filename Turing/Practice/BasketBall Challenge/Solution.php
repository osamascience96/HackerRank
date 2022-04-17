
<!-- Solved in 20 minutes -->
<!-- Prints the Solution in Linear Time O(n) -->
<!-- Ideal Time to Solve as per Turing Code Challenge = 15 minutes -->

<?php
    class Solution{
        private $inputSet;

        function __construct($inputSet){
            $this->inputSet = $inputSet;
        }

        function GetOps(){
            $total = 0;
            $newRecord = array();

            for($i=0; $i < count($this->inputSet); $i++){
                
                $currentSize = count($newRecord);

                if($this->inputSet[$i] == "+"){
                   $value1 = intval($newRecord[$currentSize-1]);
                   $value2 = intval($newRecord[$currentSize-2]);
                   
                   $sum = $value1 + $value2;

                   array_push($newRecord, $sum);
                }else if($this->inputSet[$i] == "D"){
                    $prev_score = intval($newRecord[$currentSize-1]);

                    $double_scr = $prev_score * 2;

                    array_push($newRecord, $double_scr);
                }else if($this->inputSet[$i] == "C"){
                    array_pop($newRecord);
                }else{
                    array_push($newRecord, intval($this->inputSet[$i]));
                }
                
                $total = array_sum($newRecord);
            }

            return $total;
        }
    }

    // Read the json input file
    $inputs = json_decode(file_get_contents("input.json"), true);
    foreach($inputs as $input){
        $solution = new Solution($input);
        print_r($solution->GetOps() . "\n");
    }
?>