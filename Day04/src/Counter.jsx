import React, { useState } from "react";

function PartyVoteCounter() {
    const [partyACount, setPartyACount] = useState(0);
    const [partyBCount, setPartyBCount] = useState(0);

    function handlePartyAClick() {
        setPartyACount(i => i + 1);
    }

    function handlePartyBClick() {
        setPartyBCount(i => i + 1);
    }

    return (
        <div style={{ textAlign: "center", marginTop: "20px" }}>
            <h1>Vote Counter</h1>
            <div >
                <button
                    onClick={handlePartyAClick}
                  
                >
                    Party A
                </button>
                <button
                    onClick={handlePartyBClick}
                    
                >
                    Party B
                </button>
            </div>
            <div>
                <p style={{ fontSize: "18px" }}>Party A Votes: {partyACount}</p>
                <p style={{ fontSize: "18px" }}>Party B Votes: {partyBCount}</p>
            </div>
        </div>
    );
}

export default PartyVoteCounter;
