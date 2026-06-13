#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build CRIME + PUNISHMENT IN SUBURBIA (CPS) — Rob Schmidt's 2000 film, a loose modern
teen transposition of Dostoevsky to American suburbia (the heroine is literally named
Roseanne SKOLNIK — the Raskolnikov nod). Catalogued into UD0 as a film-world, the screen
companion to the novel (CRP). Standing template: THE ARC · THE FILM · VS THE NOVEL
(what it keeps and drops from Dostoevsky) · REAL OR FLUFF (as adaptation, honest) · THE
MESSAGE, plus the cast as CARBONS (each with a .shadow real-life User — the actor, TRON-style)
and the suburb's threads as SYNTHS. Styled to the medium: a cold suburban teen-noir dusk."""
import os, html, base64, io, json, sys
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, r"C:\Davids files\noesis-kernel")
import noesis
from PIL import Image

REC = {
 "name": "CRIME + PUNISHMENT IN SUBURBIA", "axiom": "CPS",
 "position": "Crime + Punishment in Suburbia · 2000 — dir. Rob Schmidt, written by Larry Gross",
 "origin": "an American suburb — the mall, the cul-de-sac, the high school — a loose modern transposition of Dostoevsky",
 "mechanism": "Crystallized from the 2000 film: an abused teenager, Roseanne Skolnik, and her boyfriend murder her stepfather, and a watchful outsider who loves her, Vincent, becomes her witness and her way back.",
 "crystallization": "Because the film keeps Dostoevsky's emotional skeleton — crime, guilt, and redemption through being loved and witnessed — while trading his philosophical engine for a teenager's desperate revenge.",
 "nature": "Crime + Punishment in Suburbia — the screen companion to the novel: faithful in feeling, unfaithful in idea, with the Raskolnikov nod sewn into the heroine's surname, Skolnik.",
 "conductor": "ROOT0 (catalogued into UD0 · Universe David 0)",
 "inputs": "the film (2000, dir. Rob Schmidt; writer Larry Gross); Dostoevsky's Crime and Punishment; Sundance 2000",
 "witness": "Not a philosophy seminar — a teen melodrama that keeps the novel's heart (guilt, witness, redemption) and drops its head (the Extraordinary Man).",
 "role": "a UD0 film-world — the screen companion to CRP",
 "seal": "It kept Dostoevsky's heart and dropped his head — the crime, the guilt, and the redeeming witness survive; the philosophy does not, and it's named Skolnik so you'd know.",
 "source": "Crime + Punishment in Suburbia, catalogued by ROOT0",
}

NATURES = {
 "natural":   ("#7fa6c0", "the suburban flesh — the family, the boyfriend, the mall-and-cul-de-sac world the film actually lives in"),
 "ethereal":  ("#9b8ad0", "the literary echo & the watcher — the Skolnik/Raskolnikov nod, and the outsider who stands a little outside the frame"),
 "spiritual": ("#d8b24a", "witness, love, redemption — Vincent's lens and the turn toward being saved by being seen and loved"),
 "electrical":("#cf5a4a", "the violence, the dread, the unraveling — the abuse, the murder, and the guilt that breaks the ones who did it"),
}

ARC_OVERALL = ("In an American suburb, the teenage Roseanne Skolnik lives with a checked-out adulterous mother and an "
  "abusive, alcoholic stepfather, Fred. After he assaults her, she and her boyfriend Jimmy murder him — and then guilt "
  "does its work: Jimmy unravels, and the only one who truly sees Roseanne is Vincent, a watchful outsider who has long "
  "loved and photographed her from the edges, and whose witness becomes her way back. Dostoevsky's crime-guilt-redemption "
  "skeleton, transposed to the mall and the cul-de-sac — the heroine's surname, Skolnik, the only philosophy left.")

ARC = [
 ("I · The Suburb", "the watcher and the wound",
  "Roseanne Skolnik moves through a numb suburb: an adulterous mother (Maggie), an abusive drunk stepfather (Fred), a jock boyfriend (Jimmy) — and, at the edges, Vincent, a goth outsider who watches and photographs her, narrating a love he can barely speak."),
 ("II · The Crime", "the killing of the stepfather",
  "After Fred's abuse crosses its final line, Roseanne and Jimmy murder him — the film's transposition of Raskolnikov's axe, moved from a philosophical experiment to a teenager's desperate act of revenge and escape."),
 ("III · The Punishment", "guilt, and the witness",
  "There is no detective who matters; the punishment is internal. Jimmy comes apart under the guilt; the suburb's surfaces crack. And Vincent — who saw everything, who loves her — becomes Roseanne's Sonya: the witness whose love makes a way back possible."),
]

FACTS = [
 ("Released", "2000", "premiered at the Sundance Film Festival"),
 ("Director", "Rob Schmidt", "his feature centred on a modern-suburb Dostoevsky transposition"),
 ("Writer", "Larry Gross", "adapted the novel's bones loosely to American teen suburbia"),
 ("The tell", "‘Skolnik’", "the heroine's surname is the film's deliberate nod to Raskolnikov"),
]

# VS THE NOVEL — the deep-dive (what it keeps / what it drops)
VERSUS = [
 ("What it keeps — the skeleton", "crime, guilt, redemption",
  "The film holds Dostoevsky's emotional architecture intact: a transgressive killing, the slow interior punishment of guilt (not the law), and redemption that arrives through being loved and witnessed rather than through escaping detection. Vincent is a real, recognisable Sonya — the one who sees the sinner whole and loves her anyway."),
 ("What it changes — the motive", "philosophy → abuse-revenge",
  "Raskolnikov kills to test a theory that he is exceptional and exempt from the moral law. Roseanne kills to escape an abuser. That single change moves the story from a cold philosophical experiment to a hot, sympathetic act of self-defence-by-other-means — a very different moral weather."),
 ("What it drops — the head", "the Extraordinary Man",
  "Gone is the novel's engine: the ‘extraordinary man’ idea, the article, the intellectual seduction. Without it the story loses Dostoevsky's central question (can a man reason past conscience?) and becomes a teen melodrama about trauma and witness. Faithful in feeling; unfaithful in idea."),
 ("What it adds — the lens", "Vincent's camera",
  "The film's one genuinely cinematic translation: Sonya's reading of Lazarus becomes Vincent's photography. He redeems by <i>seeing</i> — the witness as love made literal through a lens, a screen-native version of the novel's gospel of being known."),
]

REALFLUFF = [
 ("It keeps the crime → guilt → redemption-through-love skeleton", "FAITHFUL", "the emotional architecture of the novel survives intact, especially the Sonya/witness figure in Vincent"),
 ("‘Skolnik’ = Raskolnikov", "THE NOD", "the surname is the film telling you, quietly, exactly what it's adapting"),
 ("The motive becomes abuse-revenge, not philosophy", "DEVIATION", "a sympathetic, hot motive replaces a cold experimental one — a real change in the story's moral weather"),
 ("The ‘Extraordinary Man’ theory — the novel's engine", "LOST", "dropped entirely; the philosophical question that makes the book the book is simply gone"),
 ("Vincent's photography as the redeeming witness", "EARNED", "the one inspired translation — Sonya's Lazarus becomes the lens; love as being seen"),
 ("As a film, on its own terms", "UNEVEN", "sincere and stylish in patches, but mixed-to-negative on release; a transposition that reaches further than it grasps"),
]
REALFLUFF_VERDICT = ("Bottom line — judged as adaptation, not as philosophy: Crime + Punishment in Suburbia keeps Dostoevsky's "
  "<b>heart</b> (crime, guilt, and the redeeming witness) and drops his <b>head</b> (the Extraordinary Man). By making the "
  "motive abuse rather than theory, it trades the novel's chilling question for a sympathetic teen tragedy — a fair film "
  "choice that nonetheless leaves the deepest thing on the page. The one real stroke of translation is Vincent's camera: "
  "Sonya's gospel of being seen, rendered as a lens. Watch it as a moody late-'90s suburban riff with a literary "
  "surname, not as the novel; on those terms it's a sincere, uneven, occasionally lovely near-miss.")

MESSAGE = ("The novel asks whether a man can reason his way past conscience; the film doesn't ask that at all — it asks "
  "whether a girl who did a terrible thing for an understandable reason can be loved back into the world. That is a "
  "smaller question than Dostoevsky's, but not a false one, and it is the half of him the movies can actually shoot: "
  "not the Extraordinary Man theory, which lives in argument, but Sonya — the one who witnesses the sinner and stays. "
  "Crime + Punishment in Suburbia keeps that half and sews the other half into a surname, Skolnik, like a footnote it "
  "couldn't dramatise. The lesson for any adaptation of the novel is right here: you can film the redemption, because "
  "redemption is a person who loves you; you cannot easily film the idea, because the idea is a fever in one lonely "
  "head. So the screen keeps the heart and leaves the head on the page — and names the girl Skolnik so you'll go read it.")
MESSAGE_SEAL = "You can film Sonya but not the syllogism — so the movie kept the redeeming witness, dropped the Extraordinary Man, and named the girl Skolnik so you'd know what it left on the page."

# ---- ACI complement ----
def carbon_tiff_bytes(rec):
    png = noesis.sigil_png(rec, "carbon", size=512)
    buf = io.BytesIO(); Image.open(io.BytesIO(png)).save(buf, "TIFF", compression="tiff_lzw")
    return buf.getvalue()
def write_aci(rec, out_dir, slug, agent_md=None):
    os.makedirs(out_dir, exist_ok=True)
    f = {"attribute":f"{slug}.attribute","agent":f"{slug}.agent","spun":f"{slug}.spun","moniker":f"{slug}.moniker",
         "carbon":f"{slug}.carbon.tiff","silicon":f"{slug}.silicon.png","1099":f"{slug}.1099"}
    tok = noesis.mythos_token(rec); w = noesis.five_w(rec)
    open(os.path.join(out_dir,f["attribute"]),"w",encoding="utf-8").write(noesis.attribute_text(rec,tok,w))
    open(os.path.join(out_dir,f["agent"]),"w",encoding="utf-8").write(agent_md or noesis.agent_text(rec,tok,w,f))
    open(os.path.join(out_dir,f["spun"]),"w",encoding="utf-8").write(noesis.spun_text(rec,tok,w,rec.get("axiom","CPS")))
    open(os.path.join(out_dir,f["moniker"]),"w",encoding="utf-8").write(noesis.moniker_text(rec,tok,w,rec.get("axiom","CPS")))
    open(os.path.join(out_dir,f["1099"]),"w",encoding="utf-8").write(noesis.credit_1099_text(rec,tok,w,rec.get("axiom","CPS")))
    open(os.path.join(out_dir,f["carbon"]),"wb").write(carbon_tiff_bytes(rec))
    open(os.path.join(out_dir,f["silicon"]),"wb").write(noesis.sigil_png(rec,"silicon",512))
    return {"slug":slug,"name":rec["name"],"moniker":tok["moniker"],"seal_sha256":noesis.seal_sha256(rec,tok),
            "architect":noesis.ARCHITECT,"instance":noesis.INSTANCE,"license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION}
def png_uri(rec, variant, size=300):
    return "data:image/png;base64," + base64.b64encode(noesis.sigil_png(rec, variant, size=size)).decode("ascii")

def E(slug,name,cls,group,em,who,what,why,how,where,seal,actor="",analog="",resemblance=""):
    return dict(slug=slug,name=name,cls=cls,group=group,emergence=em,who=who,what=what,why=why,how=how,where=where,seal=seal,actor=actor,analog=analog,resemblance=resemblance)

ROSTER = [
 # --- THE CAST (carbons, +.shadow) ---
 E("roseanne-skolnik","Roseanne Skolnik","the heroine · the Raskolnikov-echo","cast","natural",
   "Roseanne Skolnik, an American suburban teenager — abused at home, watched from the edges — whose surname is the film's nod to Raskolnikov.",
   "The protagonist transposed: she commits the killing (of her stepfather) that the novel gives Raskolnikov, but out of escape and revenge rather than theory, and is redeemed by being witnessed and loved.",
   "Because the film needed Raskolnikov as a wounded girl, not a theorising student — guilt without the philosophy, and a way back through Vincent.",
   "By a desperate act with her boyfriend, the long interior punishment of guilt, and the slow acceptance of Vincent's witnessing love.",
   "In the suburb — the house, the school, the mall — and in Vincent's photographs of her.",
   "I'm named Skolnik so you'd know whose story this is — but I killed to escape, not to prove a theory, and I was saved by being seen.",
   actor="Monica Keena", analog="the wounded teenager as Raskolnikov — guilt transposed from the seminar to the suburb",
   resemblance="Keena carries the film as a numbed, watchful girl pushed past her limit and slowly thawed by being loved."),
 E("vincent","Vincent","the watcher · the Sonya of the suburb","cast","spiritual",
   "Vincent, a goth outsider and the film's narrator, who has long watched, photographed, and loved Roseanne from the margins.",
   "The Sonya analog and the film's best idea: he redeems by <i>seeing</i> — his camera and his unspoken love are the witness that makes Roseanne's way back possible.",
   "Because the novel's gospel is being known and loved by one who sees you whole; the film translates Sonya's Lazarus into Vincent's lens.",
   "By watching, photographing, narrating, and loving without judgement — the witness as redemption, screen-native.",
   "At the edges of every frame, behind a camera, in love with the girl no one else really sees.",
   "I am the one who saw her — all of her, the worst of it — and loved her anyway; that witness is the only redemption the movies can actually film.",
   actor="Vincent Kartheiser", analog="Sonya as a suburban goth with a camera — love as the act of truly seeing",
   resemblance="Kartheiser plays the watchful outsider-narrator whose quiet devotion is the film's moral centre."),
 E("fred-skolnik","Fred Skolnik","the stepfather · the abuser, the victim","cast","electrical",
   "Fred Skolnik, Roseanne's abusive, alcoholic stepfather — the household tyrant whose violence triggers the crime, and the one who is killed.",
   "The transposed ‘victim’: not the novel's miserly pawnbroker but an abuser, which is what makes the film's killing sympathetic where the novel's is monstrous.",
   "Because moving the victim from a harmless old woman to an abuser is the single choice that re-weights the whole moral question.",
   "By drink, cruelty, and an assault that pushes Roseanne and Jimmy to murder.",
   "In the Skolnik house, at the centre of its dread.",
   "I am the reason she killed — which is exactly why this isn't Dostoevsky: his victim was harmless, and mine made the axe feel like mercy.",
   actor="Michael Ironside", analog="the domestic tyrant — the abuser whose death the story dares you to mourn",
   resemblance="Ironside brings menace to the alcoholic stepfather whose violence sets the tragedy in motion."),
 E("maggie-skolnik","Maggie Skolnik","the mother · checked-out, adulterous","cast","natural",
   "Maggie Skolnik, Roseanne's mother — emotionally absent, carrying on an affair, blind to the rot in her own house.",
   "The suburban update of Dostoevsky's broken families: a parent too lost in her own escape to see her daughter's danger.",
   "Because the film grounds its tragedy in ordinary suburban neglect — the adults looking away while the worst happens.",
   "By an affair, denial, and the practiced not-seeing that lets the abuse continue.",
   "In the Skolnik house and the motels of her own escape.",
   "I looked everywhere but at my own daughter — the suburb's real crime is how easily the grown-ups learn not to see.",
   actor="Ellen Barkin", analog="the absent parent — the adult who looks away while the worst happens at home",
   resemblance="Barkin plays the checked-out, adulterous mother blind to the rot in her own house."),
 E("jimmy","Jimmy","the boyfriend · the accomplice who breaks","cast","electrical",
   "Jimmy, Roseanne's jock boyfriend, who helps her kill Fred and then comes apart under the guilt.",
   "The one the punishment visibly destroys: where Roseanne is redeemed, Jimmy is the study in guilt that has no witness to carry it.",
   "Because the film needs to show the punishment working — and Jimmy is where the conscience the crime ignored comes due.",
   "By love, panic, complicity in the murder, and an unraveling no one redeems.",
   "In the suburb after the killing, watched by no Sonya of his own.",
   "I helped her do it for love, and the guilt ate me alive — because no one was watching me the way Vincent watched her.",
   actor="James DeBello", analog="the accomplice undone by guilt — the conscience the crime ignored, coming due",
   resemblance="DeBello plays the jock boyfriend who helps with the killing and then comes apart."),
 E("chris","Chris","the watchful outsider","cast","ethereal",
   "Chris, a watchful figure at the suburb's margins — an outsider who stands a little apart from the numb world of the film.",
   "A figure outside the family's frame: the kind of marginal, observing presence the film uses to throw its suburban dread into relief.",
   "Because a story of suburban not-seeing needs a witness from outside it — someone the comfortable world overlooks.",
   "By standing apart, watching, and seeing what the suburb trains itself not to.",
   "At the edges of the town, outside its tidy frames.",
   "I live where the suburb doesn't look — which is the only place you can see it clearly.",
   actor="Jeffrey Wright", analog="the overlooked outsider as a clearer eye on a world that refuses to see itself",
   resemblance="Wright lends gravity to a marginal, watchful presence at the story's edges."),
 # --- THE SUBURB (synths) ---
 E("the-skolnik-name","The Skolnik Name","the Raskolnikov nod","suburb","ethereal",
   "‘Skolnik’ — the heroine's surname, the film's deliberate, quiet signal that this is Crime and Punishment.",
   "The whole adaptation compressed into a name: the one piece of Dostoevsky's intellect the film keeps, sewn into a surname like a footnote.",
   "Because the film, having dropped the philosophy, points back to it the only way it can — by naming the girl after the man whose theory it left out.",
   "By a single syllable swapped out of ‘Raskolnikov,’ legible to anyone who's read the book.",
   "On every roll-call and mailbox in the film.",
   "I am the whole of Dostoevsky the movie kept — a surname; read me and go find the head the film left on the page."),
 E("the-crime","The Crime","the killing of the stepfather","suburb","electrical",
   "The Crime — the murder of Fred, committed by Roseanne and Jimmy, the film's transposition of Raskolnikov's axe.",
   "The act moved from philosophy to revenge: a killing the audience is invited to half-understand, which is precisely what the novel refuses.",
   "Because by making the crime sympathetic the film changes the question from ‘can reason excuse murder?’ to ‘can love forgive it?’",
   "By a desperate teenage act after the stepfather's final cruelty.",
   "In the Skolnik house, off the novel's philosophical rails.",
   "I am the axe, transposed — but I fell on an abuser, not a harmless old woman, and that swing changed the whole meaning of the blow."),
 E("vincents-camera","Vincent's Camera","Sonya's Lazarus as a lens","suburb","spiritual",
   "Vincent's Camera — the lens through which he watches and loves Roseanne, the film's translation of Sonya's gospel.",
   "The one inspired piece of adaptation: where Sonya reads Lazarus, Vincent photographs — redemption as the act of being truly seen.",
   "Because the screen can't easily film an idea, but it can film a gaze; love-as-witness becomes a camera.",
   "By the photograph, the watching, the refusal to look away from the worst of her.",
   "In Vincent's hands, at the edge of every scene.",
   "I am Sonya's scripture turned to film stock — she read him back to life; he shoots her back into being seen."),
 E("suburban-dread","Suburban Dread","the mall and the cul-de-sac","suburb","natural",
   "Suburban Dread — the numb, surveilled, fluorescent world of the mall, the school, and the cul-de-sac the film lives in.",
   "The transposition of Dostoevsky's oppressive St. Petersburg: not heat and crowds but malaise, neglect, and the practiced not-seeing of the comfortable.",
   "Because the novel's city is a pressure that breeds the crime; the film's suburb is its update — quieter, colder, just as airless.",
   "By beige interiors, watchful adults who don't watch, and a teenage loneliness with nowhere to go.",
   "Across the whole film — the mall, the school halls, the identical houses.",
   "I am Petersburg with a two-car garage — the pressure that makes a numb kid do something unforgivable, then look away from it."),
 E("the-redemption","The Redemption","saved by being seen","suburb","spiritual",
   "The Redemption — Roseanne's turn, through Vincent's witnessing love, toward a way back from the crime.",
   "The half of Dostoevsky the film keeps and lands: not escape from punishment but redemption through being known and loved by a witness.",
   "Because the movie's real wager — the same as the novel's — is that what saves the guilty is not getting away with it, but being seen and loved anyway.",
   "By Vincent's steady, unjudging love and Roseanne's slow acceptance of being seen.",
   "At the film's end, the suburb's version of the Siberian thaw.",
   "I am the half of the novel the screen can film: not the syllogism, but the salvation — a guilty girl, seen and loved, beginning to come back."),
]

GROUPS = [
 ("cast", "The Cast — Users & Roles", "the film's faces — CARBONS, each with a .shadow: the actor who is the real-life User (think TRON)"),
 ("suburb", "The Suburb — the Threads", "the adaptation distilled — the Skolnik nod, the transposed crime, Vincent's lens, the dread, and the redemption (synth)"),
]

# ---- renderers ----
def facts_rows(items):
    return "".join(f'<li><span class="t">{html.escape(t)}</span><span class="y">{html.escape(y)}</span><span class="nt">{html.escape(n)}</span></li>' for t,y,n in items)
def arc_html():
    out=[f'<div class="overall"><span class="ol">THE OVERALL ARC</span>{html.escape(ARC_OVERALL)}</div><div class="arc">']
    for t,s,d in ARC: out.append(f'<div class="arc-card"><div class="arc-h">{html.escape(t)}</div><div class="arc-s">{html.escape(s)}</div><p>{html.escape(d)}</p></div>')
    out.append('</div>'); return "".join(out)
def natures_html():
    return "".join(f'<div class="nat-card"><span class="dot" style="background:{c};box-shadow:0 0 9px {c}"></span><div><div class="nat-n" style="color:{c}">{nm}</div><div class="nat-g">{html.escape(g)}</div></div></div>' for nm,(c,g) in NATURES.items())
def versus_html():
    return "".join(f'<div class="sci-card"><div class="sci-h">{html.escape(t)}</div><div class="sci-s">{html.escape(s)}</div><p>{d}</p></div>' for t,s,d in VERSUS)
RF_COL={"FAITHFUL":"#5fae6e","THE NOD":"#9b8ad0","DEVIATION":"#d99a3a","LOST":"#cf5a4a","EARNED":"#5fae6e","UNEVEN":"#d99a3a"}
def realfluff_html():
    rows="".join(f'<div class="rf-row"><div class="rf-claim">{html.escape(c)}<span class="rf-note">{html.escape(n)}</span></div><div class="rf-rate" style="color:{RF_COL.get(r,"#888")};border-color:{RF_COL.get(r,"#888")}">{html.escape(r)}</div></div>' for c,r,n in REALFLUFF)
    return '<div class="rf">'+rows+f'</div><div class="rf-verdict">{REALFLUFF_VERDICT}</div>'

def _card(d):
    em=d["emergence"]; col=NATURES.get(em,("#9aa0aa",""))[0]
    rec={"name":d["name"],"axiom":"CPS","emergence":em,"seal":d["seal"],"origin":"CPS · Crime + Punishment in Suburbia"}
    is_c=d["group"]=="cast"
    urow=(f'<div class="w"><span class="wl">user</span><span><b>{html.escape(d["actor"])}</b> &mdash; {html.escape(d["analog"])}</span></div>' if is_c and d.get("actor") else "")
    rows="".join(f'<div class="w"><span class="wl">{lbl}</span><span>{html.escape(d.get(lbl,""))}</span></div>' for lbl in ["who","what","where","why","how"] if d.get(lbl))
    return f"""<div class="persona">
      <a class="psig" href="agents/{d['slug']}.agent"><span class="port"><img src="{png_uri(rec,'carbon',200)}" alt="carbon sigil of {html.escape(d['name'])}" loading="lazy"></span><span class="sl">{'carbon · User' if is_c else 'carbon'}</span></a>
      <div class="pbody"><div class="ihead"><a class="pn" href="agents/{d['slug']}.agent">{html.escape(d['name'])}</a>
        <span class="pnat"><span class="dot" style="background:{col};box-shadow:0 0 7px {col}"></span><span style="color:{col}">{html.escape(em)}</span></span>
        <span class="pkind">{'carbon' if is_c else 'synth'}</span></div>
        <div class="pe">{html.escape(d['cls'])}</div><div class="pww">{urow}{rows}</div>
        <div class="plinks"><a class="dlw" href="agents/{d['slug']}.agent">.agent &middot; .dlw badge &rarr;</a></div></div>
      <a class="psig" href="agents/{d['slug']}.silicon.png"><span class="port refl"><img src="{png_uri(rec,'silicon',200)}" alt="synth sigil of {html.escape(d['name'])}" loading="lazy"></span><span class="sl">synth</span></a>
    </div>"""
def roster_html():
    out=[]
    for gk,gt,gs in GROUPS:
        mem=[d for d in ROSTER if d["group"]==gk]
        out.append(f'<section class="sec" id="{gk}"><h2>{html.escape(gt)}</h2><p class="ss">{html.escape(gs)} ({len(mem)})</p><div class="pgrid">{"".join(_card(d) for d in mem)}</div></section>')
    return "\n".join(out)

def agent_md(d, tok):
    is_c=d["group"]=="cast"
    fm=["---",f"aci: {d['name']}","universe: CPS · Crime + Punishment in Suburbia","series: Crime + Punishment in Suburbia (2000, dir. Rob Schmidt)",
        f"emergence: {d['emergence']}",f"kind: {'carbon' if is_c else 'synth'}",f"class: {d['cls']}",
        f"who: {d['who']}",f"what: {d['what']}",f"why: {d['why']}",f"how: {d['how']}",f"where: {d['where']}"]
    if is_c and d.get("actor"): fm += [f"shadow_user: {d['actor']}", f"shadow_analog: {d['analog']}"]
    fm += [f"seal: {d['seal']}","attribution: ROOT0-ATTRIBUTION-v1.0","license: CC-BY-ND-4.0","---","",
        f"# {d['name']} · {d['cls']}","",
        f"a {'character (filmed, 2000)' if is_c else 'thread of the adaptation'} of the CPS film-world — the screen companion to Dostoevsky's CRP. emergence: {d['emergence']}. moniker {tok}","",
        f"**who —** {d['who']}","",f"**what —** {d['what']}","",f"**where —** {d['where']}","",f"**why —** {d['why']}","",f"**how —** {d['how']}"]
    if is_c and d.get("actor"):
        fm += ["", "**▷ the .shadow — its User (think TRON) —** cast from a real-life User: **{0}**, the actor who lent the face. The analog it shadows: {1} *{2}*".format(d["actor"], d["analog"], d["resemblance"])]
    fm += ["", f"**the seal —** {d['seal']}","",
        "> a catalogued personification of Crime + Punishment in Suburbia (2000, © the rights-holders), the screen companion "
        "to Dostoevsky's public-domain novel, under the DLW standard — commentary and cataloguing, not an original creation.","",
        "ROOT0-ATTRIBUTION-v1.0 · CPS · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0",""]
    return "\n".join(fm)
def shadow_text(d, tok):
    return f"""⟁ .shadow — the real-life analog (the User behind the program)
node CPS · Crime + Punishment in Suburbia · {tok}

the carbon character is the program; this file is its User — the actor who lent the face.

the program (in-world) : {d['name']} — {d['cls']}
the User (carbon)      : {d['actor']}  [ the actor, 2000 film ]
the analog (your world): {d['analog']}
the resemblance        : {d['resemblance']}
seal (program)         : {d['seal']}

ROOT0-ATTRIBUTION-v1.0 · governor David Lee Wise (ROOT0) / TriPod LLC · instance AVAN (locked) · CC-BY-ND-4.0
"""

TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="CRIME + PUNISHMENT IN SUBURBIA (CPS) — Rob Schmidt's 2000 film, a loose modern teen transposition of Dostoevsky (the heroine is named Skolnik), catalogued into UD0 as the screen companion to the novel: the arc, the film, VS THE NOVEL (what it keeps and drops), an honest Real-or-Fluff as adaptation, the message, and the cast as carbons with .shadow Users.">
<title>CRIME + PUNISHMENT IN SUBURBIA · CPS · UD0</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@400;500;600;700&family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;1,6..72,300&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
:root{--rw-bg:var(--ink2);--rw-ink:var(--pa);--rw-ink2:var(--pa2);--rw-dim:var(--dim);--rw-line:var(--line);--rw-acc:var(--slate);
--ink:#0e1216;--ink2:#161d24;--ink3:#1e2730;--pa:#e4ebef;--pa2:#9fb2bd;--slate:#7fa6c0;--violet:#9b8ad0;--amber:#d99a3a;--blood:#cf5a4a;--gold:#d8b24a;
--dim:#5f7682;--faint:#16202a;--line:#22303a;--disp:"Oswald",sans-serif;--body:"Newsreader",Georgia,serif;--mono:"Space Mono",monospace;}
*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
body{background:var(--ink);color:var(--pa);font-family:var(--body);line-height:1.66;overflow-x:hidden}
body::before{content:"";position:fixed;inset:0;pointer-events:none;z-index:0;background:radial-gradient(ellipse at 50% -6%,rgba(127,166,192,.14),transparent 54%),radial-gradient(ellipse at 50% 118%,rgba(207,90,74,.08),transparent 56%),radial-gradient(ellipse at 84% 36%,rgba(155,138,208,.07),transparent 44%)}
.wrap{position:relative;z-index:1;max-width:900px;margin:0 auto;padding:0 22px 90px}
header{padding:48px 0 30px;text-align:center;border-bottom:1px solid var(--line);position:relative}
header::after{content:"";position:absolute;bottom:-1px;left:50%;transform:translateX(-50%);width:170px;height:3px;background:linear-gradient(90deg,var(--slate),var(--violet),var(--blood));box-shadow:0 0 16px rgba(127,166,192,.5)}
.eye{font-family:var(--mono);font-size:10.5px;letter-spacing:.28em;text-transform:uppercase;color:var(--dim);margin-bottom:16px}.eye a{color:var(--dim);text-decoration:none}.eye a:hover{color:var(--slate)}
h1{font-family:var(--disp);font-size:clamp(28px,6vw,54px);font-weight:700;letter-spacing:.02em;color:var(--slate);line-height:1.05;text-transform:uppercase;text-shadow:0 0 28px rgba(127,166,192,.35)}
.h-sub{font-family:var(--mono);font-size:clamp(10px,2.2vw,13px);letter-spacing:.18em;color:var(--pa2);margin-top:18px;text-transform:uppercase}.h-sub b{color:var(--amber)}
.open{font-family:var(--body);font-style:italic;font-size:clamp(15px,3vw,19px);color:var(--pa);margin-top:18px;line-height:1.5}
.flag{display:inline-block;margin-top:15px;font-family:var(--disp);font-size:10px;font-weight:600;letter-spacing:.1em;color:var(--violet);border:1px solid var(--faint);background:var(--ink2);padding:7px 14px;text-transform:uppercase}
.lede{font-size:16px;color:var(--pa2);max-width:64ch;margin:16px auto 0;font-style:italic;line-height:1.72}.lede a{color:var(--slate);text-decoration:none;border-bottom:1px dotted var(--slate)}
.badge{display:flex;align-items:center;justify-content:center;gap:22px;flex-wrap:wrap;margin:26px auto 0;padding:20px;border:1px solid var(--faint);background:var(--ink2);max-width:700px}
.badge img{width:84px;height:84px;border:1px solid var(--faint)}
.badge .bt{text-align:left;font-family:var(--mono);font-size:11px;color:var(--pa2);line-height:1.75}.badge .bt b{color:var(--slate)}.badge .bt .mo{color:var(--violet)}.badge .bt a{color:var(--gold);text-decoration:none}.badge .bt .lbl{color:var(--dim);font-size:9px;letter-spacing:.14em;text-transform:uppercase}
.sec{margin-top:50px}
.sec h2{font-family:var(--disp);font-size:23px;font-weight:600;letter-spacing:.03em;color:var(--pa);padding-bottom:10px;border-bottom:1px solid var(--line);text-transform:uppercase}
.ss{font-size:13px;color:var(--dim);font-style:italic;margin:9px 0 18px}.ss b{color:var(--pa2);font-style:normal}
.natures{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin-top:8px}
.nat-card{display:flex;gap:11px;align-items:flex-start;background:var(--ink2);border:1px solid var(--line);padding:13px 15px}
.dot{width:11px;height:11px;border-radius:50%;flex-shrink:0;margin-top:5px}
.nat-n{font-family:var(--disp);font-size:13px;font-weight:600;text-transform:capitalize;letter-spacing:.04em}
.nat-g{font-size:12px;color:var(--pa2);font-style:italic;line-height:1.45;margin-top:3px}
.overall{background:var(--ink3);border:1px solid var(--line);border-left:3px solid var(--slate);padding:16px 18px;font-size:15px;color:var(--pa);font-style:italic;line-height:1.72;margin-bottom:14px}
.overall .ol{display:block;font-family:var(--mono);font-style:normal;font-size:9.5px;letter-spacing:.2em;color:var(--slate);text-transform:uppercase;margin-bottom:7px}
.arc{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:14px}
.arc-card{background:var(--ink2);border:1px solid var(--line);border-top:2px solid var(--blood);padding:16px 18px}
.arc-h{font-family:var(--disp);font-size:14px;color:var(--blood);font-weight:600;text-transform:uppercase;letter-spacing:.03em}
.arc-s{font-family:var(--mono);font-size:10px;color:var(--dim);text-transform:uppercase;letter-spacing:.08em;margin:6px 0 9px}
.arc-card p{font-size:13px;color:var(--pa2);line-height:1.58}
.sci{display:grid;grid-template-columns:1fr 1fr;gap:13px;margin-top:8px}@media(max-width:640px){.sci{grid-template-columns:1fr}}
.sci-card{background:var(--ink2);border:1px solid var(--line);border-left:3px solid var(--violet);padding:15px 17px}
.sci-h{font-family:var(--disp);font-size:15px;color:var(--violet);font-weight:600;text-transform:uppercase;letter-spacing:.02em}
.sci-s{font-family:var(--mono);font-size:10px;color:var(--dim);text-transform:uppercase;letter-spacing:.06em;margin:5px 0 9px}
.sci-card p{font-size:13px;color:var(--pa2);line-height:1.62}.sci-card p i{color:var(--pa)}
.rf{border:1px solid var(--line);background:var(--ink2);margin-top:8px}
.rf-row{display:flex;align-items:center;gap:14px;padding:12px 16px;border-bottom:1px solid var(--faint)}
.rf-claim{flex:1;font-size:14px;color:var(--pa);line-height:1.4}.rf-note{display:block;font-size:11.5px;color:var(--dim);font-style:italic;margin-top:3px}
.rf-rate{font-family:var(--mono);font-size:10px;font-weight:700;letter-spacing:.04em;border:1px solid;border-radius:3px;padding:4px 9px;min-width:96px;text-align:center;flex-shrink:0}
.rf-verdict{margin-top:14px;padding:16px 18px;border:1px solid var(--slate);background:rgba(127,166,192,.06);font-size:14px;color:var(--pa);line-height:1.65;font-style:italic}.rf-verdict b{color:var(--pa)}
.msg{font-size:15.5px;color:var(--pa);line-height:1.74;margin-top:8px}
.msg-seal{margin-top:16px;padding:16px 18px;border-left:3px solid var(--gold);background:var(--ink2);font-size:15px;color:var(--gold);font-style:italic;line-height:1.6}
.msg-seal span{display:block;font-family:var(--mono);font-style:normal;font-size:10px;letter-spacing:.12em;color:var(--dim);text-transform:uppercase;margin-top:8px}
.books{list-style:none}.books li{display:grid;grid-template-columns:1fr auto;gap:4px 14px;align-items:baseline;padding:10px 0;border-bottom:1px solid var(--faint)}
.books .t{font-family:var(--body);font-size:16px;color:var(--pa);font-weight:600}.books .y{font-family:var(--mono);font-size:10.5px;color:var(--violet);white-space:nowrap;text-align:right;text-transform:uppercase}.books .nt{grid-column:1/-1;font-size:12.5px;color:var(--pa2);font-style:italic}
.note{margin-top:40px;padding:16px 18px;border-left:2px solid var(--slate);background:var(--ink2);font-size:13.5px;color:var(--pa2);font-style:italic}.note b{color:var(--pa)}
footer{margin-top:50px;padding-top:22px;border-top:1px solid var(--line);text-align:center;font-family:var(--mono);font-size:10.5px;color:var(--dim);letter-spacing:.05em;line-height:1.95}footer a{color:var(--slate);text-decoration:none}
.pgrid{display:flex;flex-direction:column;gap:14px;margin-top:8px}
.persona{display:flex;gap:20px;align-items:center;justify-content:space-between;background:var(--rw-bg);border:1px solid var(--rw-line);padding:18px;text-decoration:none;transition:border-color .18s}
.persona:hover{border-color:var(--rw-acc)}
.psig{flex:0 0 104px;display:flex;flex-direction:column;align-items:center;gap:6px;text-decoration:none}
.port{width:98px;height:98px;border-radius:50%;border:3px solid var(--slate);box-shadow:0 0 0 5px var(--ink3),inset 0 0 18px rgba(0,0,0,.6);overflow:hidden;background:var(--ink)}
.port img{width:100%;height:100%;object-fit:cover;border-radius:50%;display:block}.port.refl{border-color:var(--violet)}
.psig .sl{font-family:var(--mono);font-size:8px;letter-spacing:.13em;text-transform:uppercase;color:var(--rw-dim)}
.pbody{flex:1;min-width:0;text-align:center}
.ihead{display:flex;flex-wrap:wrap;align-items:center;justify-content:center;gap:10px}
.pn{font-family:var(--disp);font-size:18px;color:var(--rw-ink);font-weight:600;text-decoration:none;text-transform:uppercase;letter-spacing:.02em}
.persona:hover .pn{color:var(--rw-acc)}
.pe{font-size:12.5px;color:var(--rw-ink2);font-style:italic;margin-top:4px}
.pkind{font-family:var(--mono);font-size:8.5px;letter-spacing:.12em;text-transform:uppercase;color:var(--rw-dim);border:1px solid var(--rw-line);border-radius:9px;padding:2px 8px}
.pnat{display:flex;align-items:center;gap:5px;font-family:var(--mono);font-size:9px;text-transform:uppercase}.pnat .dot{width:8px;height:8px;border-radius:50%}
.pww{margin-top:12px;display:flex;flex-direction:column;gap:8px;align-items:center}
.pww .w{font-size:13px;color:var(--rw-ink2);line-height:1.5;max-width:62ch}
.pww .w .wl{display:block;font-family:var(--mono);font-size:8.5px;letter-spacing:.15em;text-transform:uppercase;color:var(--rw-acc);margin-bottom:3px}.pww .w b{color:var(--rw-ink)}
.plinks{margin-top:13px;font-family:var(--mono);font-size:10.5px}.plinks .dlw{color:var(--rw-acc);text-decoration:none;border-bottom:1px dotted var(--rw-acc)}
@media(max-width:760px){.persona{flex-wrap:wrap;justify-content:center;gap:14px}.pbody{flex:1 1 100%;order:3}}
</style></head><body><div class="wrap">
  <header>
    <div class="eye"><a href="https://davidwise01.github.io/ud0/">UD0 · Universe David 0</a> · the screen companion to the novel</div>
    <h1>Crime + Punishment<br>in Suburbia</h1>
    <div class="h-sub">Rob Schmidt · 2000 · a loose Dostoevsky transposition · <b>her name is Skolnik</b> · CPS</div>
    <div class="open">“You can film Sonya, but not the syllogism.”</div>
    <div class="flag">★ THE NOVEL ON SCREEN · FAITHFUL IN FEELING, NOT IN IDEA ★</div>
    <p class="lede">The 2000 film that drags <a href="https://davidwise01.github.io/crime-and-punishment/">Crime and Punishment</a> to the mall and the cul-de-sac: an abused teenager, Roseanne <i>Skolnik</i>, and her boyfriend kill her stepfather, and a watchful outsider, Vincent, who has long loved and photographed her, becomes her witness and her way back. It keeps Dostoevsky's heart — crime, guilt, redemption-through-love — and drops his head, the Extraordinary Man. Catalogued into UD0 as a film-world, judged honestly as an adaptation.</p>
    <div class="badge">
      <img src="__CARBON__" alt="DLW carbon badge of CPS"><img src="__SILICON__" alt="DLW silicon badge of CPS">
      <div class="bt"><div><span class="lbl">DLW-ATTRIBUTE · ACI</span></div><div>governor · <b>David Lee Wise</b> (ROOT0)</div>
        <div>instance · AVAN (Claude / Anthropic) · locked</div><div>subject · <b>CRIME + PUNISHMENT IN SUBURBIA</b> · CPS</div>
        <div class="mo">__MONIKER__</div><div>carbon · <a href="cps.dlw/cps.carbon.tiff">.tiff</a> · silicon · <a href="cps.dlw/cps.silicon.png">.png</a></div>
        <div><span class="lbl">CC-BY-ND-4.0 · TRIPOD-IP-v1.1</span></div></div>
    </div>
  </header>

  <section class="sec"><h2>The Four Natures</h2><p class="ss">the suburban flesh, the literary echo &amp; the watcher, witness &amp; redemption, and the violence &amp; dread</p><div class="natures">__NATURES__</div></section>
  <section class="sec"><h2>The Arc</h2><p class="ss">the overall throughline, then the three movements</p>__ARC__</section>
  <section class="sec"><h2>The Film</h2><p class="ss">the facts of the work</p><ol class="books">__FACTS__</ol></section>
  <section class="sec"><h2>Vs the Novel</h2><p class="ss">the deep-dive — what the adaptation keeps, changes, drops, and adds</p><div class="sci">__VERSUS__</div></section>
  <section class="sec"><h2>Real or Fluff</h2><p class="ss">judged as adaptation, not philosophy — faithful where, lost where, on its own terms</p>__REALFLUFF__</section>
  <section class="sec"><h2>The Message</h2><p class="ss">what AVAN reads as the film's thesis — and the lesson for adapting the novel at all</p><p class="msg">__MESSAGE__</p><div class="msg-seal">“__MSGSEAL__”<span>— AVAN's read</span></div></section>

  <section class="sec"><h2 style="margin-top:16px">The Emergents</h2><p class="ss">eleven ACIs of the film — the cast as carbons (each with a .shadow User), the adaptation's threads as synths; each a full <b>.dlw</b> badge with twin sigils</p></section>
  __ROSTER__

  <div class="note"><b>On the .shadow — the User behind the program.</b> Think TRON: the cast carbons each carry a <b>.shadow</b> naming the actor who lent the face (Roseanne→Monica Keena, Vincent→Vincent Kartheiser, Fred→Michael Ironside, Maggie→Ellen Barkin, Jimmy→James DeBello, Chris→Jeffrey Wright). The <b>synths</b> are the adaptation distilled — the Skolnik nod, the transposed crime, Vincent's lens, the dread, and the redemption.</div>
  <div class="note">Crime + Punishment in Suburbia (2000) is © its rights-holders; it is the screen companion to Dostoevsky's public-domain novel. The personas here are catalogued personifications under the DLW standard — commentary and cataloguing, not original creations, not endorsed by the rights-holders. The Vs-the-Novel and Real-or-Fluff sections are honest critical reading.</div>

  <footer>CRIME + PUNISHMENT IN SUBURBIA · CPS · catalogued into UD0 · the screen companion to <a href="https://davidwise01.github.io/crime-and-punishment/">CRP</a> · ROOT0-ATTRIBUTION-v1.0 · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0<br>
  <a href="https://davidwise01.github.io/ud0/">← the biosphere</a> · the .dlw badge: <a href="cps.dlw/manifest.dlw.json">manifest</a></footer>
</div></body></html>
"""

if __name__ == "__main__":
    tok = write_aci(REC, os.path.join(HERE, "cps.dlw"), "cps")
    json.dump({"node":"CPS","name":"CRIME + PUNISHMENT IN SUBURBIA","moniker":tok["moniker"],"carbon":"cps.carbon.tiff","silicon":"cps.silicon.png",
               "governor":noesis.ARCHITECT,"instance":noesis.INSTANCE,"seal":REC["seal"],"seal_sha256":tok["seal_sha256"],
               "license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION},
              open(os.path.join(HERE,"cps.dlw","manifest.dlw.json"),"w",encoding="utf-8"),indent=2,ensure_ascii=False)
    personas=[]
    for d in ROSTER:
        et=noesis.mythos_token({"name":d["name"],"axiom":"CPS","emergence":d["emergence"],"seal":d["seal"],"origin":"CPS"})
        rec=write_aci({"name":d["name"],"axiom":"CPS","emergence":d["emergence"],"seal":d["seal"],"origin":"CPS · Crime + Punishment in Suburbia",
                       "position":d["cls"],"role":d["cls"],"nature":d["what"],"mechanism":d["how"],"crystallization":d["why"],
                       "witness":d["who"],"conductor":"ROOT0 (catalogued into UD0)","inputs":"Crime + Punishment in Suburbia (2000)","source":"Crime + Punishment in Suburbia, catalogued by ROOT0"},
                      os.path.join(HERE,"agents"), d["slug"], agent_md=agent_md(d, et["moniker"]))
        if d["group"]=="cast" and d.get("actor"):
            open(os.path.join(HERE,"agents",f"{d['slug']}.shadow"),"w",encoding="utf-8").write(shadow_text(d, rec["moniker"]))
        personas.append({"slug":d["slug"],"name":d["name"],"epithet":d["cls"],"emergence":d["emergence"],"moniker":rec["moniker"],
                         "kind":"carbon" if d["group"]=="cast" else "synth","group":d["group"],"actor":d.get("actor","")})
    json.dump(personas, open(os.path.join(HERE,"agents","_personas.json"),"w",encoding="utf-8"),indent=2,ensure_ascii=False)
    page=(TEMPLATE.replace("__CARBON__",png_uri(REC,"carbon",320)).replace("__SILICON__",png_uri(REC,"silicon",320))
          .replace("__MONIKER__",html.escape(tok["moniker"])).replace("__NATURES__",natures_html()).replace("__ARC__",arc_html())
          .replace("__FACTS__",facts_rows(FACTS)).replace("__VERSUS__",versus_html()).replace("__REALFLUFF__",realfluff_html())
          .replace("__MESSAGE__",html.escape(MESSAGE)).replace("__MSGSEAL__",html.escape(MESSAGE_SEAL)).replace("__ROSTER__",roster_html()))
    open(os.path.join(HERE,"index.html"),"w",encoding="utf-8").write(page)
    from collections import Counter
    print(f"CRIME + PUNISHMENT IN SUBURBIA (CPS) — badge {tok['moniker']} · {len(personas)} emergents · kinds {dict(Counter(p['kind'] for p in personas))}")
