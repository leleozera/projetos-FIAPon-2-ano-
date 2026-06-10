import { useState, useEffect } from "react"
import { ScatterChart, Scatter, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, Cell } from "recharts"
import axios from "axios"
import "./index.css"

const API = "http://localhost:8000"
const CORES = ["#4caf7d", "#cc4444", "#a0a0a0"]

export default function App() {
  const [tela, setTela] = useState("objetos")
  const [dados, setDados] = useState(null)
  const [analise, setAnalise] = useState(null)
  const [loading, setLoading] = useState(true)
  const [pergunta, setPergunta] = useState("")
  const [mensagens, setMensagens] = useState([])
  const [chatLoading, setChatLoading] = useState(false)

  useEffect(() => {
    Promise.all([
      axios.get(`${API}/dados`),
      axios.get(`${API}/analise`)
    ]).then(([r1, r2]) => {
      setDados(r1.data)
      setAnalise(r2.data)
      setLoading(false)
    }).catch(() => setLoading(false))
  }, [])

  async function enviar() {
    if (!pergunta.trim()) return
    const p = pergunta
    setPergunta("")
    setMensagens(prev => [...prev, { role: "user", text: p }])
    setChatLoading(true)
    try {
      const res = await axios.post(`${API}/chat`, { pergunta: p })
      setMensagens(prev => [...prev, { role: "ai", text: res.data.resposta }])
    } catch {
      setMensagens(prev => [...prev, { role: "ai", text: "Erro ao conectar com a IA." }])
    }
    setChatLoading(false)
  }

  if (loading) return <div className="loading">Carregando dados da NASA...</div>

  const { stats, clusters, objects } = analise || {}

  return (
    <div className="app">
      <div className="header">
        <h1>Galax IA</h1>
        <p>Monitoramento inteligente de objetos próximos à Terra </p>
      </div>

      <div className="tabs">
        {["objetos", "analise", "chat"].map(t => (
          <button key={t} className={`tab ${tela === t ? "active" : ""}`} onClick={() => setTela(t)}>
            {t === "objetos" ? "Objetos" : t === "analise" ? "Análise ML" : "Chat IA"}
          </button>
        ))}
      </div>

      {tela === "objetos" && dados && (
        <>
          <div className="cards">
            <div className="card"><h3>Total de objetos</h3><p>{dados.total}</p></div>
            <div className="card"><h3>Objetos Perigosos</h3><p>{stats?.potencialmente_perigosos}</p></div>
            <div className="card"><h3>Vel. média</h3><p>{stats?.velocidade_media_km_h?.toLocaleString("pt-BR")} km/h</p></div>
            <div className="card"><h3>Dist. média</h3><p>{(stats?.distancia_media_km / 1000000).toFixed(1)}M km</p></div>
          </div>

          <div className="table-container">
            <h2>Objetos detectados — últimos 7 dias</h2>
            <table>
              <thead>
                <tr>
                  <th>Nome</th><th>Data</th><th>Velocidade (km/h)</th><th>Distância (km)</th><th>Diâmetro (km)</th><th>Status</th>
                </tr>
              </thead>
              <tbody>
                {dados.objetos.map(obj => (
                  <tr key={obj.id}>
                    <td>{obj.name}</td>
                    <td>{obj.date}</td>
                    <td>{Number(obj.velocity_km_h).toLocaleString("pt-BR")}</td>
                    <td>{Number(obj.miss_distance_km).toLocaleString("pt-BR")}</td>
                    <td>{obj.diameter_max_km.toFixed(4)}</td>
                    <td>
                      <span className={`badge ${obj.is_hazardous ? "danger" : "safe"}`}>
                        {obj.is_hazardous ? "Perigoso" : "Seguro"}
                      </span>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </>
      )}

      {tela === "analise" && analise && (
        <>
          <div className="chart-container">
            <h2>Clusters por velocidade e distância</h2>
            <ResponsiveContainer width="100%" height={350}>
              <ScatterChart>
                <CartesianGrid strokeDasharray="3 3" stroke="#1e1e1e" />
                <XAxis dataKey="velocity_km_h" name="Velocidade" stroke="#444" tickFormatter={v => `${(v/1000).toFixed(0)}k`} />
                <YAxis dataKey="miss_distance_km" name="Distância" stroke="#444" tickFormatter={v => `${(v/1000000).toFixed(0)}M`} />
                <Tooltip cursor={{ fill: "#ffffff08" }} contentStyle={{ background: "#141414", border: "1px solid #222", color: "#ccc" }} />
                <Scatter data={objects} fill="#4caf7d">
                  {objects?.map((obj, i) => (
                    <Cell key={i} fill={CORES[obj.cluster] || "#4caf7d"} />
                  ))}
                </Scatter>
              </ScatterChart>
            </ResponsiveContainer>
          </div>

          <div className="clusters">
            {clusters?.map(c => (
              <div key={c.cluster} className="cluster-card">
                <h3>Grupo {c.cluster}</h3>
                <p>Vel. média: {c.velocity_km_h?.toLocaleString("pt-BR")} km/h</p>
                <p>Dist. média: {c.miss_distance_km?.toLocaleString("pt-BR")} km</p>
                <p>Diâm. médio: {c.diameter_max_km} km</p>
              </div>
            ))}
          </div>
        </>
      )}

      {tela === "chat" && (
        <div className="chat-container">
          <h2>Pergunte à IA sobre os dados</h2>
          <div className="messages">
            {mensagens.map((m, i) => (
              <div key={i} className={`message ${m.role}`}>
                {m.text.split("\n").map((linha, j) =>
                  linha.trim() === "" ? <br key={j} /> : <p key={j}>{linha}</p>
                )}
              </div>
            ))}
            {chatLoading && <div className="message ai"><p>Processando...</p></div>}
          </div>
          <div className="chat-input">
            <input
              value={pergunta}
              onChange={e => setPergunta(e.target.value)}
              onKeyDown={e => e.key === "Enter" && enviar()}
              placeholder="Ex: Quais objetos são potencialmente perigosos?"
            />
            <button onClick={enviar}>Enviar</button>
          </div>
        </div>
      )}
    </div>
  )
}