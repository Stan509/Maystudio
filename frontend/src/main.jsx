import React, { useEffect, useMemo, useState } from 'react';
import { createRoot } from 'react-dom/client';
import { BrowserRouter, Link } from 'react-router-dom';
import { MapPin, Phone, Menu, X, CalendarDays, Home, Sparkles, ArrowRight, CheckCircle2 } from 'lucide-react';
import { QRCodeCanvas } from 'qrcode.react';
import './styles.css';

const API = import.meta.env.VITE_API_URL || 'http://127.0.0.1:8000/api';
const flyer = '/assets/maystudio-flyer.png';
const logo = '/assets/maystudio-logo.jpeg';
const source = '/assets/maystudio-banner-source.jpeg';

const fallbackServices = [
  ['African braids','Tresses africaines'],
  ['Box braids','Tresses box'],
  ['Cornrows','Nattes collées'],
  ['Senegalese twists','Torsades sénégalaises'],
  ['Twists & braids','Torsades et tresses'],
  ['Weaves & wigs','Tissages et perruques'],
  ["Men’s hairstyles",'Coiffures pour hommes'],
];

const fallbackGallery = Array.from({length: 6}, (_, i) => ({id:i+1, title:'MAY STUDIO style', image_url:source}));

function App(){
  const [lang,setLang] = useState('en');
  const [open,setOpen] = useState(false);
  const [services,setServices] = useState([]);
  const [gallery,setGallery] = useState([]);
  const [settings,setSettings] = useState(null);

  useEffect(()=>{
    Promise.all([
      fetch(`${API}/services/`).then(r=>r.ok?r.json():[]).catch(()=>[]),
      fetch(`${API}/gallery/`).then(r=>r.ok?r.json():[]).catch(()=>[]),
      fetch(`${API}/settings/`).then(r=>r.ok?r.json():null).catch(()=>null),
    ]).then(([s,g,st])=>{
      setServices(s);
      setGallery(g);
      setSettings(st);
    });
  },[]);

  const t = useMemo(()=>({
    navHome: lang==='en'?'Home':'Accueil',
    navServices: lang==='en'?'Services':'Services',
    navGallery: lang==='en'?'Gallery':'Galerie',
    navBooking: lang==='en'?'Book now':'Réserver',
    heroKicker: lang==='en'?'AFRICAN HAIR STYLIST':'SPÉCIALISTE DES COIFFURES AFRICAINES',
    heroTitle: lang==='en'?'Your Hair, Our Passion':'Vos cheveux, notre passion',
    heroText: lang==='en'?'Braids, cornrows, twists and beautiful African hairstyles for women and men.':'Tresses, nattes, torsades et coiffures africaines pour femmes et hommes.',
    book: lang==='en'?'Book your appointment':'Réservez votre rendez-vous',
    special: lang==='en'?'Hair Special':'Spécial Coiffure',
    servicesTitle: lang==='en'?'Our Services':'Nos Services',
    galleryTitle: lang==='en'?'Signature Styles':'Nos styles signature',
    locationTitle: lang==='en'?'Visit the studio':'Venez au studio',
    homeTitle: lang==='en'?'Home service available':'Service à domicile disponible',
    homeText: lang==='en'?'On order / by request':'Sur commande / sur demande',
    scan: lang==='en'?'Scan to visit our website':'Scannez pour visiter notre site',
    phone: settings?.phone || '+1 845 263 6492',
    address: settings?.address || '10 Harding Ave, Haverstraw, New York',
    price: settings?.special_price || 80,
  }),[lang,settings]);

  const serviceItems = services.length ? services : fallbackServices.map((x,i)=>({id:i,name_en:x[0],name_fr:x[1]}));
  const galleryItems = gallery.length ? gallery : fallbackGallery;

  return <div className="app">
    <header className="nav">
      <Link className="brand" to="/" onClick={()=>setOpen(false)}>
        <img src={logo} alt="MAY STUDIO logo" />
        <span>MAY <small>STUDIO</small></span>
      </Link>
      <nav className={open?'nav-links open':'nav-links'}>
        <a href="#home" onClick={()=>setOpen(false)}>{t.navHome}</a>
        <a href="#services" onClick={()=>setOpen(false)}>{t.navServices}</a>
        <a href="#gallery" onClick={()=>setOpen(false)}>{t.navGallery}</a>
        <a href="#booking" onClick={()=>setOpen(false)}>{t.navBooking}</a>
      </nav>
      <div className="nav-actions">
        <a className="phone" href={`tel:${t.phone.replace(/\s/g,'')}`}><Phone size={16}/>{t.phone}</a>
        <button className="lang" onClick={()=>setLang(lang==='en'?'fr':'en')}>{lang==='en'?'FR':'EN'}</button>
        <button className="mobile-menu" aria-label="Menu" onClick={()=>setOpen(!open)}>{open?<X/>:<Menu/>}</button>
      </div>
    </header>

    <main>
      <section id="home" className="hero section-pad">
        <div className="hero-copy">
          <div className="eyebrow">MAY STUDIO • {t.heroKicker}</div>
          <h1>{t.heroTitle}</h1>
          <p>{t.heroText}</p>
          <div className="hero-buttons">
            <a href="#booking" className="btn btn-gold">{t.book}<ArrowRight size={18}/></a>
            <a href={`tel:${t.phone.replace(/\s/g,'')}`} className="btn btn-ghost"><Phone size={18}/> {lang==='en'?'Call us':'Appelez-nous'}</a>
          </div>
          <div className="hero-meta">
            <span><Sparkles size={16}/> {lang==='en'?'Women & Men':'Femmes & Hommes'}</span>
            <span><Home size={16}/> {lang==='en'?'Home service':'À domicile'}</span>
          </div>
        </div>
        <div className="hero-art">
          <div className="hero-image-wrap">
            <img src={flyer} alt="MAY STUDIO hairstyles" />
          </div>
          <div className="special-card"><span>{t.special}</span><strong>${t.price}</strong></div>
        </div>
      </section>

      <section id="services" className="section section-dark">
        <div className="section-head">
          <div><span className="eyebrow">MAY STUDIO</span><h2>{t.servicesTitle}</h2></div>
          <p>{lang==='en'?'Authentic African styling, finished with precision.':'Des coiffures africaines authentiques, réalisées avec précision.'}</p>
        </div>
        <div className="service-grid">
          {serviceItems.map((s,i)=><article className="service-card" key={s.id||i}>
            <div className="service-index">0{i+1}</div>
            <h3>{lang==='en'?s.name_en:s.name_fr}</h3>
            <p>{lang==='en'?(s.description_en||'Custom African hairstyle'): (s.description_fr||'Coiffure africaine sur mesure')}</p>
          </article>)}
        </div>
      </section>

      <section id="gallery" className="section section-cream">
        <div className="section-head dark-text">
          <div><span className="eyebrow">STYLE • CONFIDENCE</span><h2>{t.galleryTitle}</h2></div>
          <p>{lang==='en'?'Explore signature looks for women and men.':'Découvrez nos styles signature pour femmes et hommes.'}</p>
        </div>
        <div className="gallery-grid">
          {galleryItems.map((g,i)=><figure className={`gallery-item gi-${i%6}`} key={g.id||i}><img src={g.image_url.startsWith('http')?g.image_url:source} alt={g.alt_text||g.title}/><figcaption>{g.title}</figcaption></figure>)}
        </div>
      </section>

      <section id="location" className="section location-section">
        <div className="location-card">
          <div className="location-copy"><span className="eyebrow">MAY STUDIO • HAVERSTRAW</span><h2>{t.locationTitle}</h2><p><MapPin size={18}/>{t.address}</p><p><Phone size={18}/>{t.phone}</p><a className="text-link" href="https://www.google.com/maps/search/?api=1&query=10+Harding+Ave+Haverstraw+NY" target="_blank">{lang==='en'?'Open in Google Maps':'Ouvrir dans Google Maps'} <ArrowRight size={16}/></a></div>
          <div className="map-visual"><div className="pin"><MapPin size={30}/></div><div className="map-lines"></div></div>
        </div>
      </section>

      <section className="home-service section-pad">
        <div className="home-icon"><Home size={34}/></div>
        <div><span className="eyebrow">ON REQUEST</span><h2>{t.homeTitle}</h2><p>{t.homeText}</p></div>
        <a href="#booking" className="btn btn-dark">{t.book}<ArrowRight size={18}/></a>
      </section>

      <section id="booking" className="section booking-section">
        <Booking lang={lang} services={serviceItems} />
      </section>
    </main>

    <footer className="footer">
      <div className="footer-brand"><img src={logo} alt="MAY STUDIO"/><div><strong>MAY STUDIO</strong><span>Beauty • Style • Confidence</span></div></div>
      <div className="footer-contact"><a href={`tel:${t.phone.replace(/\s/g,'')}`}><Phone size={17}/>{t.phone}</a><span><MapPin size={17}/>{t.address}</span></div>
      <div className="footer-qr"><QRCodeCanvas value="https://maystudio.shop" size={74} bgColor="#fff" fgColor="#111" level="H" /><span>{t.scan}<br/><strong>maystudio.shop</strong></span></div>
    </footer>
  </div>
}

function Booking({lang,services}){
  const [form,setForm]=useState({name:'',phone:'',email:'',service:'',preferred_date:'',preferred_time:'',notes:'',home_service:false});
  const [sent,setSent]=useState(false); const [error,setError]=useState('');
  const update=(e)=>{const {name,value,type,checked}=e.target; setForm({...form,[name]:type==='checkbox'?checked:value});};
  const submit=async(e)=>{
    e.preventDefault(); setError('');
    try{
      const r=await fetch(`${API}/bookings/`,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(form)});
      if(!r.ok){throw new Error('booking failed');}
      setSent(true);
      setForm({name:'',phone:'',email:'',service:'',preferred_date:'',preferred_time:'',notes:'',home_service:false});
    }catch(_){setError(lang==='en'?'Please call us directly to confirm your appointment.':'Appelez-nous directement pour confirmer votre rendez-vous.');}
  };
  return <div className="booking-wrap">
    <div className="booking-intro"><span className="eyebrow">BOOKING / RÉSERVATION</span><h2>{lang==='en'?'Reserve your look':'Réservez votre coiffure'}</h2><p>{lang==='en'?'Tell us what you want and we’ll confirm your appointment.':'Dites-nous ce que vous souhaitez et nous confirmerons votre rendez-vous.'}</p><div className="booking-proof"><CheckCircle2 size={18}/>{lang==='en'?'Women & men welcome':'Femmes & hommes bienvenus'}</div><div className="booking-proof"><CheckCircle2 size={18}/>{lang==='en'?'Home service by request':'Service à domicile sur demande'}</div></div>
    <form className="booking-form" onSubmit={submit}>
      {sent && <div className="success">{lang==='en'?'Request received. We’ll contact you shortly.':'Demande reçue. Nous vous contacterons bientôt.'}</div>}
      {error && <div className="error">{error}</div>}
      <div className="form-grid">
        <input name="name" value={form.name} onChange={update} required placeholder={lang==='en'?'Full name':'Nom complet'} />
        <input name="phone" value={form.phone} onChange={update} required placeholder={lang==='en'?'Phone':'Téléphone'} />
        <input name="email" type="email" value={form.email} onChange={update} placeholder="Email" />
        <select name="service" value={form.service} onChange={update} required><option value="">{lang==='en'?'Choose a service':'Choisir un service'}</option>{services.map((s,i)=><option key={s.id||i} value={s.name_en}>{lang==='en'?s.name_en:s.name_fr}</option>)}</select>
        <input name="preferred_date" type="date" value={form.preferred_date} onChange={update} required />
        <input name="preferred_time" type="time" value={form.preferred_time} onChange={update} required />
      </div>
      <textarea name="notes" value={form.notes} onChange={update} placeholder={lang==='en'?'Anything we should know?':'Une précision à nous communiquer ?'} rows="4"></textarea>
      <label className="check-row"><input type="checkbox" name="home_service" checked={form.home_service} onChange={update}/><span>{lang==='en'?'I’m requesting home service':'Je demande le service à domicile'}</span></label>
      <button className="btn btn-gold" type="submit"><CalendarDays size={18}/>{lang==='en'?'Send booking request':'Envoyer la demande'}</button>
    </form>
  </div>
}

createRoot(document.getElementById('root')).render(<BrowserRouter><App/></BrowserRouter>);
