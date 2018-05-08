pragma solidity ^0.4.18;

contract Greet {
    string public greeting;

    function Greet() {
        greeting = 'Hello';
    }

    function setGreeting(string _greeting) public {
        greeting = _greeting;
    }

    function greet() constant returns (string) {
        return greeting;
    }
}
