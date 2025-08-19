import { useState, useEffect } from "react";

function App() {
  const [joke, setJoke] = useState(null);    
  const [loading, setLoading] = useState(true); 
  const [error, setError] = useState(null);     

  // fungsi ambil data joke
  async function fetchJoke() {
    setLoading(true);
    setError(null);

    try {
      const response = await fetch(
        "https://v2.jokeapi.dev/joke/Any?blacklistFlags=racist,sexist&type=single"
      );

      if (!response.ok) throw new Error("Gagal mengambil data");

      const data = await response.json();
      setJoke(data.joke); // dari API, text joke ada di field "joke"
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }

  // otomatis jalan sekali waktu pertama kali load
  useEffect(() => {
    fetchJoke();
  }, []);

  return (
    <div style={{ textAlign: "center", padding: "20px" }}>
      <h1>😂 Joke Random 😂</h1>

      {/* kondisi loading */}
      {loading && <p>Memuat...</p>}

      {/* kondisi error */}
      {error && <p style={{ color: "red" }}>Error: {error}</p>}

      {/* kalau joke berhasil */}
      {joke && <p>{joke}</p>}

      {/* tombol untuk ambil joke baru */}
      <button onClick={fetchJoke} style={{ marginTop: "20px" }}>
        🔄 Joke Baru
      </button>
    </div>
  );
}

export default App;
