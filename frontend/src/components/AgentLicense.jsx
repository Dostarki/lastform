import { useEffect, useRef } from 'react';
import { Copy, Download, Fingerprint } from 'lucide-react';
import { Button } from './ui/button';
import { toast } from './ui/sonner';
import { drawLicense, saveLicense, copyLicense } from '../lib/license';
import { numberLabel } from '../lib/api';

export const AgentLicense = ({ agent, handle }) => {
  const canvas = useRef(null);
  useEffect(() => {
    let active = true;
    drawLicense(canvas.current, agent, handle);
    document.fonts.ready.then(() => { if (active && canvas.current) drawLicense(canvas.current, agent, handle); });
    return () => { active = false; };
  }, [agent, handle]);
  return <section className="license-section" aria-label="Your agent license" data-testid="agent-license-section">
    <div className="section-label"><Fingerprint size={14} /><span data-testid="license-heading">PERSONNEL FILE</span><span className="license-state" data-testid="license-state">{agent ? numberLabel(agent.number) : 'UNREGISTERED'}</span></div>
    <div className="license-paper"><span className="license-tape" aria-hidden="true" /><canvas ref={canvas} className="license-canvas" role="img" aria-label={`Agent license for @${agent?.handle || handle}. ${agent ? `Number ${agent.number}, class ${agent.agent_class}, cell ${agent.cell}, tier ${agent.tier}.` : 'Awaiting registration.'}`} data-testid="agent-license-canvas" /></div>
    <div className="license-actions"><Button variant="ghost" onClick={() => copyLicense(canvas.current, agent?.handle || handle)} data-testid="copy-card-button"><Copy size={14} /> Copy image</Button><Button variant="ghost" onClick={() => saveLicense(canvas.current, agent?.handle || handle).catch(() => toast.error('Could not export your card.'))} data-testid="save-card-button"><Download size={14} /> Save card</Button></div>
  </section>;
};