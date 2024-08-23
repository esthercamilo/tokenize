pragma solidity ^0.8.26;

contract EvaluationPlatform {
    struct User {
        string name;
        address userAddress;
        uint tokens;
        string[] badges;
    }

    mapping(address => User) public users;

    function addUser(string memory _name) public {
        users[msg.sender] = User(_name, msg.sender, 0, new string[](0));
    }

    function awardTokens(address _user, uint _amount) public {
        users[_user].tokens += _amount;
    }

    function awardBadge(address _user, string memory _badge) public {
        users[_user].badges.push(_badge);
    }

    function getUser(address _user) public view returns (string memory, uint, string[] memory) {
        User memory user = users[_user];
        return (user.name, user.tokens, user.badges);
    }
}
