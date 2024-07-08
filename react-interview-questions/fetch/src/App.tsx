import React, { useEffect, useState } from "react";

function App() {
  const [results, setResults] = useState<any[]>([]);
  useEffect(() => {
    fetch("https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=2")
    .then((res) => res.json())
    .then((data) => {
      console.log('data', JSON.stringify(data, null, 2));

      setResults(data)
    })

  }, []);

  return (
    <div style={{ flexDirection: "column" }}>
      {results.map((res) => (
        <div key={res._id}>{res.type}</div>
      ))}
    </div>
  );
}

export default App;
