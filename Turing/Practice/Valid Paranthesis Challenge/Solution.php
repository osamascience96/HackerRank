<!-- This is the Famous Bracket Paranthesis Problem -->
<!-- Solved in Linear Time, Searching for the Constant Time to Solve this Problem -->
<!-- Ideal time to solve is 10 minutes -->
<!-- Time Taken: 35 minutes -->
<!-- Performance: Low -->

<?php
    class Solution{
        
        private $input;

        function __construct($input)
        {
            $this->input = $input;
        }

        function ValidateParenthesis(){
            $is_valid = false;

            $leftCharStack = array();

            for($i=0; $i < strlen($this->input); $i++){
                
                $char = $this->input[$i];
                
                if($char == "{" || $char == "(" || $char == "["){
                    array_push($leftCharStack, $char);
                }else{
                    if(empty($leftCharStack)){
                        break;
                    }

                    $popedChar = array_pop($leftCharStack);

                    if($char == ")"&&$popedChar=="(" || $char == "}"&&$popedChar=="{" || $char == "]"&&$popedChar=="["){
                        $is_valid = true;
                    }else{
                        $is_valid = false;
                    }
                } 
            }

            if(!empty($leftCharStack)){
                $is_valid = false;
            }

            return $is_valid == true ? "valid" : "invalid";
        }
    }

    $inputs = json_decode(file_get_contents("input.json"));
    foreach($inputs as $input){
        $solution = new Solution($input);
        print_r($solution->ValidateParenthesis() . "\n");
    }
?>