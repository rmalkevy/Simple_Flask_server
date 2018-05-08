var Greet = artifacts.require("./Greet.sol");

module.exports = function(deployer) {
  deployer.deploy(Greet);
};
