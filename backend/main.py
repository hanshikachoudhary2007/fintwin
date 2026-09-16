{\rtf1\ansi\ansicpg1252\cocoartf2870
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # backend/main.py\
from fastapi import FastAPI\
from fastapi.middleware.cors import CORSMiddleware\
import networkx as nx\
import random\
\
app = FastAPI()\
\
app.add_middleware(\
    CORSMiddleware,\
    allow_origins=["*"],\
    allow_methods=["*"],\
    allow_headers=["*"],\
)\
\
# Mock Data Generator for "Coastal Entrepreneurs" Group\
def get_group_data():\
    members = [\
        \{"id": 1, "name": "Elena R.", "income": 1200, "debt": 400, "dna": "Stable", "xp": 850\},\
        \{"id": 2, "name": "Marcus T.", "income": 800, "debt": 600, "dna": "Sensitive", "xp": 420\},\
        \{"id": 3, "name": "Amina B.", "income": 1500, "debt": 200, "dna": "Resilient", "xp": 980\},\
        \{"id": 4, "name": "Kofi A.", "income": 950, "debt": 700, "dna": "At-Risk", "xp": 310\},\
    ]\
    # Exposure Graph: Who is connected to whom?\
    connections = [(1, 2), (2, 4), (3, 1), (4, 3)]\
    return members, connections\
\
@app.get("/api/group-status")\
def group_status():\
    members, connections = get_group_data()\
    \
    # Calculate Group Trust Score (Gamification)\
    avg_xp = sum(m['xp'] for m in members) / len(members)\
    level = "Resilient" if avg_xp > 700 else "Developing"\
    \
    return \{\
        "group_name": "Coastal Entrepreneurs",\
        "level": level,\
        "total_xp": avg_xp,\
        "members": members,\
        "connections": connections,\
        "next_reward": "5% Interest Rate Reduction"\
    \}\
\
@app.get("/api/simulate-shock")\
def simulate_shock(member_id: int):\
    # FinTwin Propagation Simulator\
    # If Kofi (4) defaults, how does it affect others?\
    members, connections = get_group_data()\
    G = nx.Graph()\
    G.add_edges_from(connections)\
    \
    affected = list(nx.single_source_shortest_path_length(G, member_id, cutoff=1).keys())\
    \
    return \{\
        "origin_shock": member_id,\
        "cascading_risk": affected,\
        "severity": "Medium",\
        "intervention": "Emergency Grace Period recommended for Node " + str(affected)\
    \}\
\
if __name__ == "__main__":\
    import uvicorn\
    uvicorn.run(app, host="0.0.0.0", port=8000)}