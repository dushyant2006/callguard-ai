"use client";

import { useEffect, useState } from "react";
import { Bell, ShieldAlert, Activity, CheckCircle, ShieldCheck, Server, XCircle, Search } from "lucide-react";
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table";
import { LineChart, Line, ResponsiveContainer, XAxis, YAxis, Tooltip, AreaChart, Area } from "recharts";

const data = [
  { time: "08:00", risk: 10 },
  { time: "09:00", risk: 15 },
  { time: "10:00", risk: 85 },
  { time: "11:00", risk: 30 },
  { time: "12:00", risk: 90 },
  { time: "13:00", risk: 20 },
];

export default function Dashboard() {
  const [alerts, setAlerts] = useState([
    { id: 1, phone: "+1 (555) 019-2834", risk: 95, type: "Scam", reason: "IRS Gift Card pattern detected." },
    { id: 2, phone: "+1 (555) 012-9981", risk: 88, type: "Phishing", reason: "Bank account credential request." },
  ]);

  return (
    <div className="min-h-screen bg-[#0a0a0a] text-zinc-100 p-8 font-sans selection:bg-blue-500/30">
      <header className="flex items-center justify-between mb-8 border-b border-zinc-800 pb-4">
        <div className="flex items-center gap-3">
          <div className="bg-blue-600/20 p-2 rounded-lg border border-blue-500/30">
            <ShieldCheck className="text-blue-400 w-6 h-6" />
          </div>
          <div>
            <h1 className="text-2xl font-bold tracking-tight bg-gradient-to-r from-white to-zinc-400 bg-clip-text text-transparent">CallGuard AI</h1>
            <p className="text-xs text-zinc-500">Enterprise Fraud Prevention Platform</p>
          </div>
        </div>
        <div className="flex items-center gap-4">
          <div className="flex items-center gap-2 text-sm text-zinc-400 bg-zinc-900 px-3 py-1.5 rounded-full border border-zinc-800">
            <Server className="w-4 h-4 text-emerald-400" /> API: Healthy
          </div>
          <Button variant="outline" size="sm" className="bg-zinc-900 border-zinc-800 text-zinc-300 hover:bg-zinc-800 hover:text-white transition-all">
            <Bell className="w-4 h-4 mr-2" /> 
            Live Alerts
            <span className="ml-2 bg-red-500 text-white text-[10px] px-1.5 py-0.5 rounded-full animate-pulse">2</span>
          </Button>
        </div>
      </header>

      <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
        <Card className="bg-zinc-900/50 border-zinc-800 backdrop-blur-sm">
          <CardHeader className="pb-2">
            <CardTitle className="text-zinc-400 text-sm font-medium flex items-center justify-between">
              Total Calls Screened
              <Activity className="w-4 h-4 text-blue-400" />
            </CardTitle>
          </CardHeader>
          <CardContent>
            <div className="text-3xl font-bold text-white">24,591</div>
            <p className="text-xs text-zinc-500 mt-1">+12% from last hour</p>
          </CardContent>
        </Card>
        
        <Card className="bg-zinc-900/50 border-zinc-800 backdrop-blur-sm relative overflow-hidden group">
          <div className="absolute inset-0 bg-red-500/5 opacity-0 group-hover:opacity-100 transition-opacity" />
          <CardHeader className="pb-2">
            <CardTitle className="text-zinc-400 text-sm font-medium flex items-center justify-between">
              High Risk Blocked
              <ShieldAlert className="w-4 h-4 text-red-400" />
            </CardTitle>
          </CardHeader>
          <CardContent>
            <div className="text-3xl font-bold text-red-400">1,204</div>
            <p className="text-xs text-red-400/70 mt-1">Scams & Phishing</p>
          </CardContent>
        </Card>

        <Card className="bg-zinc-900/50 border-zinc-800 backdrop-blur-sm relative overflow-hidden group">
          <div className="absolute inset-0 bg-emerald-500/5 opacity-0 group-hover:opacity-100 transition-opacity" />
          <CardHeader className="pb-2">
            <CardTitle className="text-zinc-400 text-sm font-medium flex items-center justify-between">
              Safe Calls Allowed
              <CheckCircle className="w-4 h-4 text-emerald-400" />
            </CardTitle>
          </CardHeader>
          <CardContent>
            <div className="text-3xl font-bold text-emerald-400">23,387</div>
            <p className="text-xs text-emerald-400/70 mt-1">Verified contacts</p>
          </CardContent>
        </Card>

        <Card className="bg-zinc-900/50 border-zinc-800 backdrop-blur-sm">
          <CardHeader className="pb-2">
            <CardTitle className="text-zinc-400 text-sm font-medium flex items-center justify-between">
              AI Confidence Average
              <Search className="w-4 h-4 text-purple-400" />
            </CardTitle>
          </CardHeader>
          <CardContent>
            <div className="text-3xl font-bold text-purple-400">96.8%</div>
            <p className="text-xs text-zinc-500 mt-1">Multi-agent consensus</p>
          </CardContent>
        </Card>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <Card className="lg:col-span-2 bg-zinc-900/50 border-zinc-800 backdrop-blur-sm">
          <CardHeader>
            <CardTitle className="text-white font-medium">Live Risk Heatmap</CardTitle>
            <CardDescription className="text-zinc-400">Real-time volume of high-risk incoming calls.</CardDescription>
          </CardHeader>
          <CardContent className="h-[300px]">
            <ResponsiveContainer width="100%" height="100%">
              <AreaChart data={data}>
                <defs>
                  <linearGradient id="colorRisk" x1="0" y1="0" x2="0" y2="1">
                    <stop offset="5%" stopColor="#ef4444" stopOpacity={0.3}/>
                    <stop offset="95%" stopColor="#ef4444" stopOpacity={0}/>
                  </linearGradient>
                </defs>
                <XAxis dataKey="time" stroke="#52525b" fontSize={12} tickLine={false} axisLine={false} />
                <YAxis stroke="#52525b" fontSize={12} tickLine={false} axisLine={false} />
                <Tooltip 
                  contentStyle={{ backgroundColor: '#18181b', border: '1px solid #27272a', borderRadius: '8px' }}
                  itemStyle={{ color: '#ef4444' }}
                />
                <Area type="monotone" dataKey="risk" stroke="#ef4444" strokeWidth={2} fillOpacity={1} fill="url(#colorRisk)" />
              </AreaChart>
            </ResponsiveContainer>
          </CardContent>
        </Card>

        <Card className="bg-zinc-900/50 border-zinc-800 backdrop-blur-sm">
          <CardHeader>
            <CardTitle className="text-white font-medium flex items-center gap-2">
              <span className="relative flex h-3 w-3">
                <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-red-400 opacity-75"></span>
                <span className="relative inline-flex rounded-full h-3 w-3 bg-red-500"></span>
              </span>
              Alert Center
            </CardTitle>
            <CardDescription className="text-zinc-400">AI reasoning for flagged calls.</CardDescription>
          </CardHeader>
          <CardContent>
            <div className="space-y-4">
              {alerts.map((alert) => (
                <div key={alert.id} className="p-4 rounded-lg bg-zinc-800/50 border border-zinc-700/50 relative overflow-hidden group">
                  <div className="absolute left-0 top-0 bottom-0 w-1 bg-red-500" />
                  <div className="flex justify-between items-start mb-2">
                    <span className="text-sm font-medium text-white">{alert.phone}</span>
                    <Badge variant="destructive" className="bg-red-500/20 text-red-400 border-0 hover:bg-red-500/30">
                      Risk: {alert.risk}%
                    </Badge>
                  </div>
                  <p className="text-xs text-zinc-400 mb-3"><span className="text-zinc-300">Reason:</span> {alert.reason}</p>
                  <div className="flex gap-2">
                    <Button size="sm" variant="outline" className="w-full text-xs h-8 bg-zinc-900 border-zinc-700 hover:bg-emerald-500/20 hover:text-emerald-400 hover:border-emerald-500/30">
                      <CheckCircle className="w-3 h-3 mr-1" /> Allow
                    </Button>
                    <Button size="sm" variant="outline" className="w-full text-xs h-8 bg-zinc-900 border-zinc-700 hover:bg-red-500/20 hover:text-red-400 hover:border-red-500/30">
                      <XCircle className="w-3 h-3 mr-1" /> Block
                    </Button>
                  </div>
                </div>
              ))}
            </div>
          </CardContent>
        </Card>
      </div>

      <Card className="mt-6 bg-zinc-900/50 border-zinc-800 backdrop-blur-sm overflow-hidden">
        <Table>
          <TableHeader className="bg-zinc-900">
            <TableRow className="border-zinc-800 hover:bg-transparent">
              <TableHead className="text-zinc-400 h-10">Caller ID</TableHead>
              <TableHead className="text-zinc-400 h-10">Timestamp</TableHead>
              <TableHead className="text-zinc-400 h-10">Classification</TableHead>
              <TableHead className="text-zinc-400 h-10">Status</TableHead>
              <TableHead className="text-zinc-400 h-10 text-right">Confidence</TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            <TableRow className="border-zinc-800 hover:bg-zinc-800/50 transition-colors">
              <TableCell className="font-medium text-zinc-300">+1 (202) 555-0198</TableCell>
              <TableCell className="text-zinc-500">2 mins ago</TableCell>
              <TableCell><Badge variant="outline" className="text-emerald-400 border-emerald-500/30 bg-emerald-500/10">Legit</Badge></TableCell>
              <TableCell className="text-zinc-400">Allowed</TableCell>
              <TableCell className="text-right text-emerald-400">99.2%</TableCell>
            </TableRow>
            <TableRow className="border-zinc-800 hover:bg-zinc-800/50 transition-colors">
              <TableCell className="font-medium text-zinc-300">Unknown Caller</TableCell>
              <TableCell className="text-zinc-500">14 mins ago</TableCell>
              <TableCell><Badge variant="outline" className="text-red-400 border-red-500/30 bg-red-500/10">Robocall</Badge></TableCell>
              <TableCell className="text-zinc-400">Blocked</TableCell>
              <TableCell className="text-right text-red-400">94.1%</TableCell>
            </TableRow>
          </TableBody>
        </Table>
      </Card>
    </div>
  );
}
