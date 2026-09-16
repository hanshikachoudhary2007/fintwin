{\rtf1\ansi\ansicpg1252\cocoartf2870
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 from fastapi import FastAPI\
from fastapi.middleware.cors import CORSMiddleware\
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
@app.get("/")\
def read_root():\
    return \{"message": "FinTwin API is Live"\}\
\
@app.get("/api/group-status")\
def group_status():\
    return \{\
        "group_name": "Coastal Entrepreneurs",\
        "level": "Resilient",\
        "total_xp": 720,\
        "next_reward": "5% Interest Relaxation",\
        "members": [\
            \{"id": 1, "name": "Elena R.", "income": 1200, "dna": "Resilient", "xp": 850\},\
            \{"id": 2, "name": "Marcus T.", "income": 800, "dna": "Sensitive", "xp": 420\},\
            \{"id": 3, "name": "Amina B.", "income": 1500, "dna": "Resilient", "xp": 980\},\
            \{"id": 4, "name": "Kofi A.", "income": 950, "dna": "At-Risk", "xp": 310\}\
        ]\
    \}}