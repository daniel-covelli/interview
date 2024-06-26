import React, { useEffect, useState } from "react";

function App() {
  const [results, setResults] = useState<any[]>([]);
  useEffect(() => {
    (async () => {
      const result = await (
        await fetch(
          "https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=2"
        )
      ).json();
      console.log("res", JSON.stringify(result, null, 2));

      setResults(result);
    })();
  }, []);

  return (
    <div style={{ flexDirection: "column" }}>
      {results.map((res) => (
        <div id={res._id}>{res.type}</div>
      ))}
    </div>
  );
}

export default App;
