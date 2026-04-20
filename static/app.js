const TITLES = {
    home: ['Home', 'Know before you go. Know before you spend.'],
    business: ['Business Transparency', 'Search any business, brand, or law enforcement agency'],
    travel: ['Safe Travel Guide', 'Search any US city, state, or full address'],
    route: ['Route Planner', 'Check safety ratings for your entire journey'],
    about: ['About & Sources', 'Learn about Conscious Consumer and our data sources']
};

const HIGH_RISK_STATES = ['Alabama','Arkansas','Florida','Georgia','Idaho','Indiana','Iowa','Kansas','Kentucky','Louisiana','Mississippi','Missouri','Montana','Nebraska','North Dakota','Ohio','Oklahoma','South Carolina','South Dakota','Tennessee','Texas','Utah','West Virginia','Wyoming'];

const ALL_COMPANIES = [
    // Retail / Shopping
    'Walmart','Amazon','Target','Costco','Home Depot','Lowes','Kroger','Walgreens','CVS',
    'Dollar General','Dollar Tree','Shein','Fashion Nova','TJ Maxx','Marshalls','Ross',
    'Macys','Nordstrom','Gap','Old Navy','H&M','Zara','Forever 21','Nike','Adidas',
    'Under Armour','Best Buy','Ebay','Etsy','Wayfair','IKEA','Sephora','Ulta',
    'Bath and Body Works',"Victoria's Secret",'Ralph Lauren','Patagonia','REI',
    'Burlington','Five Below','Aldi','Trader Joes','Whole Foods','Sprouts',
    'Publix','Safeway','Albertsons','Instacart','Shipt','Chewy','PetSmart','Petco',

    // Fast Food / Restaurants
    "McDonald's",'Starbucks','Chick-fil-A','Burger King','Taco Bell',"Wendy's",
    'Subway',"Domino's",'Pizza Hut','Chipotle','Dunkin','Popeyes','KFC','Sonic',
    'Dairy Queen','Five Guys','In-N-Out','Shake Shack','Panda Express','Olive Garden',
    "Applebee's",'IHOP',"Denny's",'Red Lobster','Panera',"Papa John's",'Little Caesars',
    'Cracker Barrel','Texas Roadhouse','Buffalo Wild Wings','Chilis','Outback Steakhouse',
    'Jack in the Box','Carl\'s Jr','Hardees','Whataburger','Wingstop','Raising Canes',
    'Dutch Bros','Jamba Juice','Smoothie King',

    // Technology
    'Apple','Google','Microsoft','Meta','Twitter/X','Netflix','Uber','Lyft','Airbnb',
    'TikTok','Snap','Spotify','Adobe','Salesforce','Oracle','IBM','Intel','Nvidia',
    'AMD','Qualcomm','Cisco','Dell','HP','Samsung','Sony','PayPal','Shopify','Zoom',
    'Discord','DoorDash','Instacart','Grubhub','Robinhood','Coinbase','Stripe','Square',
    'Palantir','Cloudflare','Dropbox','Slack','Twitter','LinkedIn','Pinterest','Reddit',
    'Twitch','YouTube','Hulu','Disney Plus','Peacock','Paramount Plus','HBO Max',

    // Banking / Finance
    'JPMorgan','Bank of America','Wells Fargo','Citibank','Goldman Sachs','Morgan Stanley',
    'American Express','Visa','Mastercard','Discover','Capital One','Chase','US Bank',
    'Charles Schwab','Fidelity','Vanguard','BlackRock','Coinbase','Robinhood',
    'TD Bank','PNC Bank','Truist','Regions Bank','SunTrust','Citizens Bank',
    'Navy Federal','USAA','Ally Bank','Marcus by Goldman Sachs','Synchrony',
    'Experian','Equifax','TransUnion','H&R Block','TurboTax','Intuit',

    // Healthcare / Pharma
    'Johnson & Johnson','Pfizer','Moderna','Merck','AbbVie','Eli Lilly','Novartis',
    'Roche','Bayer','Purdue Pharma','CVS Health','UnitedHealth','Anthem','Cigna',
    'Aetna','Humana','HCA Healthcare','Tenet Health','Kaiser Permanente',
    'Walgreens Boots Alliance','McKesson','AmerisourceBergen','Cardinal Health',
    'DaVita','Fresenius','Davita','Kindred Healthcare','Envision Healthcare',

    // Energy / Oil
    'Exxon','Chevron','Shell','BP','ConocoPhillips','Halliburton','Duke Energy',
    'NextEra Energy','Tesla Energy','First Solar','Dominion Energy','Southern Company',
    'Entergy','Exelon','PG&E','Con Edison','National Grid','Sunrun','Vivint Solar',
    'Schlumberger','Baker Hughes','Marathon Oil','Valero','Phillips 66',

    // Food & Beverage
    'Coca-Cola','Pepsi','Nestlé','Unilever','Kraft Heinz','General Mills',"Kellogg's",
    'Tyson Foods','Smithfield','Beyond Meat','Impossible Foods','Cargill','ADM',
    'Conagra','Campbell Soup','Hormel','Dole','Chobani','Danone','Monster Beverage',
    'Red Bull','Anheuser-Busch','Molson Coors','Constellation Brands','Brown-Forman',
    'Philip Morris','Altria','RJ Reynolds','JM Smucker','McCormick','Land O Lakes',

    // Insurance
    'State Farm','Allstate','Geico','Progressive','Liberty Mutual','USAA','Nationwide',
    'AIG','Aflac','Travelers','Hartford Financial','Chubb','Zurich','MetLife',
    'Prudential','New York Life','Northwestern Mutual','Unum','Principal Financial',

    // Telecom / Media
    'AT&T','Verizon','T-Mobile','Xfinity','Spectrum','Cox','Dish Network',
    'DirecTV','Comcast','Charter','Frontier','CenturyLink','Lumen Technologies',
    'Disney','Warner Bros','NBCUniversal','Paramount','Fox Corporation','News Corp',
    'ViacomCBS','Discovery','AMC Networks','iHeartMedia','Clear Channel',

    // Automotive
    'Tesla','Ford','General Motors','Toyota','Honda','Volkswagen','BMW','Mercedes',
    'Volvo','Subaru','Rivian','Carvana','CarMax','AutoNation','Penske Automotive',
    'Stellantis','Chrysler','Jeep','Ram','Dodge','Hyundai','Kia','Mazda','Nissan',
    'Mitsubishi','Porsche','Audi','Land Rover','Jaguar',

    // Travel / Hospitality
    'Marriott','Hilton','Delta Airlines','United Airlines','American Airlines',
    'Southwest Airlines','Carnival Cruise','Royal Caribbean','Norwegian Cruise',
    'Hyatt','IHG','Wyndham','Choice Hotels','Best Western','Airbnb','Expedia',
    'Booking.com','Priceline','Tripadvisor','Hertz','Enterprise','Avis','Budget',
    'Spirit Airlines','Frontier Airlines','JetBlue','Alaska Airlines',

    // Defense / Government Contractors
    'Lockheed Martin','Raytheon','Boeing','Northrop Grumman','General Dynamics',
    'L3Harris','Leidos','Booz Allen Hamilton','SAIC','ManTech','DXC Technology',
    'Accenture','Deloitte','KPMG','PricewaterhouseCoopers','Ernst & Young',

    // Private Prisons
    'GEO Group','CoreCivic',

    // Agriculture
    'Monsanto','Bayer CropScience','Syngenta','BASF','Corteva','Deere & Company',
    'Perdue Farms','Sanderson Farms','Pilgrim\'s Pride','Wayne Farms',

    // Gig / Staffing
    'DoorDash','Uber Eats','Grubhub','TaskRabbit','Fiverr','Upwork',
    'Manpower','Robert Half','Adecco','Kelly Services','Randstad',

    // Real Estate
    'Blackstone','Invitation Homes','American Homes 4 Rent','Zillow','Redfin',
    'RE/MAX','Keller Williams','Coldwell Banker','CBRE','Jones Lang LaSalle',

    // Education
    'University of Phoenix','DeVry','Grand Canyon University','Strayer University',
    'Pearson','McGraw Hill','Chegg','Duolingo','Coursera','Khan Academy',

    // Law Enforcement
    'Minneapolis Police Department','Los Angeles Police Department',
    'Chicago Police Department','Houston Police Department',
    'New York Police Department','Philadelphia Police Department'
];

const DATA_SOURCES = {
    'source-fec': { title: 'Federal Election Commission', description: 'The FEC tracks all political donations by corporations and PACs. We use this data to identify companies with significant political spending, particularly in ways that may conflict with consumer interests.', url: 'https://www.fec.gov', impact: 'Up to 40 points deducted based on committee count and donation patterns.' },
    'source-news': { title: 'NewsAPI', description: 'We scan recent news headlines for negative coverage including lawsuits, fraud, violations, penalties, and controversies. Only verified news sources are included.', url: 'https://newsapi.org', impact: 'Up to 30 points deducted based on negative headline count.' },
    'source-court': { title: 'CourtListener / RECAP Archive', description: "Free Law Project's CourtListener provides access to federal court records. We search for cases involving each company and factor in the volume of litigation.", url: 'https://www.courtlistener.com', impact: 'Up to 30 points deducted based on federal case count.' },
    'source-mpv': { title: 'Mapping Police Violence', description: 'A comprehensive database tracking all known police killings in the US, maintained by researchers and updated regularly. Used for both travel safety ratings and law enforcement agency scoring.', url: 'https://mappingpoliceviolence.us', impact: 'Used for travel safety ratings and law enforcement agency business scores.' },
    'source-hrc': { title: 'HRC Corporate Equality Index', description: "The Human Rights Campaign's annual rating of major employers on LGBTQ+ workplace policies.", url: 'https://www.hrc.org', impact: 'Informs state-level LGBTQ+ safety ratings and travel advisories.' },
    'source-naacp': { title: 'NAACP Travel Advisories', description: 'The NAACP issues travel advisories for states with documented threats to Black Americans and other communities of color.', url: 'https://naacp.org', impact: 'Directly informs state racial safety ratings.' },
    'source-esg': { title: 'Sustainalytics ESG Data', description: 'ESG risk scores based on Sustainalytics methodology. Higher scores indicate greater ESG risk. Our dataset covers 400+ companies.', url: 'https://www.sustainalytics.com', impact: 'Up to 25 points deducted based on ESG risk rating.' },
    'source-bhr': { title: 'Business & Human Rights Resource Centre', description: 'Tracks human rights impacts of business globally, including labor rights, supply chain abuses, and community impacts.', url: 'https://www.business-humanrights.org', impact: 'Up to 25 points deducted based on human rights risk rating.' },
    'source-eeoc': { title: 'Equal Employment Opportunity Commission', description: 'The EEOC enforces federal laws prohibiting employment discrimination. We track EEOC lawsuits and settlements against companies across all five protected community categories.', url: 'https://www.eeoc.gov', impact: 'Up to 20 points deducted based on case count and communities affected.' },
    'source-nlrb': { title: 'National Labor Relations Board', description: 'The NLRB tracks unfair labor practice charges against employers including union-busting, illegal surveillance, and retaliation against organizing workers.', url: 'https://www.nlrb.gov', impact: 'Up to 20 points deducted based on charge count and severity.' },
    'source-map': { title: 'Movement Advancement Project', description: 'MAP tracks 50+ LGBTQ+ laws and policies in all 50 states and DC, including nondiscrimination laws, conversion therapy bans, healthcare protections, and anti-trans legislation.', url: 'https://mapresearch.org', impact: 'Directly informs state LGBTQ+ safety ratings with law-by-law detail.' },
    'source-doj': { title: 'DOJ Civil Rights Division', description: 'The Department of Justice Civil Rights Division enforces federal laws prohibiting discrimination. We surface civil rights enforcement actions and settlements across all five community categories.', url: 'https://www.justice.gov/crt', impact: 'Informs community flag source links for BIPOC, LGBTQ+, Women, Disability, and Workers.' },
    'source-osm': { title: 'OpenStreetMap', description: 'Free, open-source mapping data maintained by a global community. Used to supplement Google Places for rest stops, accessible amenities, and public facilities along routes.', url: 'https://www.openstreetmap.org', impact: 'Used for safe stop recommendations along driving routes.' },
    'source-corpwatch': { title: 'CorpWatch', description: 'Extracts subsidiary relationship data from SEC 10-K filings, mapping corporate family trees including parent companies, subsidiaries, and countries of operation.', url: 'http://api.corpwatch.org', impact: 'Displayed as corporate structure transparency information.' }
};

const COMMUNITIES_INFO = {
    lgbtq: { label: 'LGBTQ+ Community', description: 'We track state nondiscrimination laws, conversion therapy bans, same-sex adoption protections, anti-trans legislation, and active HRC travel advisories.' },
    racial: { label: 'Racial & Ethnic Minorities', description: 'We track NAACP travel advisories, voting rights restrictions, racial disparities in criminal justice, and documented racial profiling concerns.' },
    religious: { label: 'Religious Minorities', description: 'We track accommodations for non-Christian travelers, RFRA laws that may permit discrimination, and local religious diversity.' },
    disability: { label: 'People with Disabilities', description: 'We track ADA compliance, accessible transportation availability, and terrain accessibility for each state.' },
    women: { label: 'Women', description: 'We track reproductive healthcare access, abortion restrictions, and legal protections in each state.' }
};

function updateSourceCount() {
    ['source-count', 'source-count-business', 'source-count-card'].forEach(id => {
        const el = document.getElementById(id);
        if (el) el.textContent = Object.keys(DATA_SOURCES).length;
    });
}

function updateCompanyCount() {
    const countEls = document.querySelectorAll('.stat-card-num, .stat-num');
    countEls.forEach(el => {
        if (el.nextElementSibling && el.nextElementSibling.textContent.includes('Companies')) {
            el.textContent = ALL_COMPANIES.length + '+';
        }
    });
}

function switchPanel(panel) {
    document.querySelectorAll('.panel').forEach(p => p.classList.remove('active'));
    ['home','business','travel','route','about'].forEach(id => {
        ['nav-','mob-','tab-'].forEach(prefix => {
            const el = document.getElementById(prefix + id);
            if (el) el.classList.remove('active');
        });
    });
    document.getElementById('panel-' + panel).classList.add('active');
    ['nav-','mob-','tab-'].forEach(prefix => {
        const el = document.getElementById(prefix + panel);
        if (el) el.classList.add('active');
    });
    
    window.scrollTo(0, 0);
}

// ===== RING ANIMATION =====
function animateRing(score) {
    const circumference = 2 * Math.PI * 40;
    const fill = document.getElementById('ringFill');
    if (!fill) return;
    fill.style.strokeDasharray = `0 ${circumference}`;
    setTimeout(() => {
        const progress = (score / 100) * circumference;
        fill.style.strokeDasharray = `${progress} ${circumference}`;
    }, 100);
}

// ===== COMMUNITY FLAGS =====
function getCommunityFlags(data) {
    const flags = data.flags || [];
    const flagText = flags.join(' ').toLowerCase();
    const esg = (data.esg_data || {});
    const hr = (data.human_rights_data || {});
    const fec = (data.fec_data || {});
    const legal = (data.legal_data || {});

    const communities = [
        {
            id: 'bipoc',
            label: 'BIPOC',
            check: () => {
                const triggers = ['indigenous', 'racial', 'discrimination', 'civil rights', 'naacp', 'racial justice', 'minority'];
                return triggers.some(t => flagText.includes(t));
            },
            warnText: 'Racial discrimination concerns documented',
            okText: 'No specific BIPOC concerns found',
            source: legal.found ? 'View court records' : null,
            sourceType: 'court'
        },
        {
            id: 'lgbtq',
            label: 'LGBTQ+',
            check: () => {
                const triggers = ['lgbtq', 'gay', 'transgender', 'pride', 'sexual orientation', 'gender identity', 'hrc'];
                return triggers.some(t => flagText.includes(t));
            },
            warnText: 'LGBTQ+ concerns or political opposition found',
            okText: 'No specific LGBTQ+ concerns found',
            source: fec.found ? 'View FEC records' : null,
            sourceType: 'fec'
        },
        {
            id: 'women',
            label: 'Women',
            check: () => {
                const triggers = ['women', 'gender pay', 'sexual harassment', 'abortion', 'reproductive', 'maternity', 'gender discrimination'];
                return triggers.some(t => flagText.includes(t));
            },
            warnText: 'Gender discrimination or pay gap concerns documented',
            okText: 'No specific concerns for women found',
            source: legal.found ? 'View court records' : null,
            sourceType: 'court'
        },
        {
            id: 'workers',
            label: 'Workers',
            check: () => {
                const triggers = ['labor', 'worker', 'wage', 'union', 'employee', 'workplace', 'safety violation', 'osha'];
                return triggers.some(t => flagText.includes(t));
            },
            warnText: 'Labor violations or worker safety issues on record',
            okText: 'No specific worker concerns found',
            source: data.news_data && data.news_data.found ? 'View news coverage' : null,
            sourceType: 'news'
        },
        {
            id: 'disability',
            label: 'Disability',
            check: () => {
                const triggers = ['disability', 'ada', 'accessibility', 'accommodation'];
                return triggers.some(t => flagText.includes(t));
            },
            warnText: 'ADA violations or accessibility concerns documented',
            okText: 'No specific disability concerns found',
            source: legal.found ? 'View court records' : null,
            sourceType: 'court'
        }
    ];

    return communities.map(c => {
        const hasIssue = c.check();
        return {
            ...c,
            hasIssue
        };
    });
}

function renderCommunityFlags(data, drawerMode = false) {
    const communities = getCommunityFlags(data);
    const sourceLinks = {
        court: `https://www.courtlistener.com/?q=${encodeURIComponent(data.business)}`,
        fec: `https://www.fec.gov/data/committees/?q=${encodeURIComponent(data.business)}`,
        news: `https://newsapi.org`
    };

    return `
        <div class="community-flags-title">Community Impact</div>
        <div class="community-flags-grid">
            ${communities.map(c => `
                <div class="comm-flag ${c.hasIssue ? 'warn' : 'ok'}" onclick="openCommunityDrawer('${c.id}', '${data.business}', ${c.hasIssue})">
                    <div class="comm-flag-label">${c.label}</div>
                    <div class="comm-flag-text">${c.hasIssue ? c.warnText : c.okText}</div>
                    ${c.hasIssue && c.source ? `<a href="${sourceLinks[c.sourceType]}" target="_blank" class="comm-flag-link">${c.source} →</a>` : ''}
                </div>`).join('')}
        </div>`;
}

function openCommunityDrawer(communityId, businessName, hasIssue) {
    const info = COMMUNITIES_INFO[communityId === 'bipoc' ? 'racial' : communityId === 'workers' ? 'racial' : communityId];
    const labels = { bipoc: 'BIPOC', lgbtq: 'LGBTQ+', women: 'Women', workers: 'Workers', disability: 'Disability' };

    document.getElementById('drawerTitle').textContent = `${labels[communityId]} — ${businessName}`;
    document.getElementById('drawerVerdict').textContent = hasIssue ? 'Concerns documented' : 'No specific concerns found';
    document.getElementById('drawerScoreSection').innerHTML = '';
    document.getElementById('drawerActions').innerHTML = `
        <button class="btn-primary" onclick="closeDrawer(); quickBusinessSearch('${businessName}')">Back to Results</button>
    `;

    const sourceLinks = {
        bipoc: { label: 'Search Court Records', url: `https://www.courtlistener.com/?q=${encodeURIComponent(businessName)}` },
        lgbtq: { label: 'Search FEC Records', url: `https://www.fec.gov/data/committees/?q=${encodeURIComponent(businessName)}` },
        women: { label: 'Search Court Records', url: `https://www.courtlistener.com/?q=${encodeURIComponent(businessName)}` },
        workers: { label: 'Search News Coverage', url: `https://newsapi.org` },
        disability: { label: 'Search Court Records', url: `https://www.courtlistener.com/?q=${encodeURIComponent(businessName)}` }
    };

    document.getElementById('drawerBody').innerHTML = `
        ${hasIssue ? `
        <div style="background:var(--coral-100); padding:14px; border-radius:8px; margin-bottom:14px;">
            <div style="font-size:0.75em; font-weight:700; text-transform:uppercase; letter-spacing:1px; color:#8a2020; margin-bottom:6px;">What We Found</div>
            <div style="font-size:0.85em; color:#8a2020; line-height:1.6;">Our data sources indicate concerns related to ${labels[communityId]} communities for ${businessName}. Review the source records for full details.</div>
        </div>` : `
        <div style="background:var(--teal-faint); padding:14px; border-radius:8px; margin-bottom:14px;">
            <div style="font-size:0.75em; font-weight:700; text-transform:uppercase; letter-spacing:1px; color:#0f6e56; margin-bottom:6px;">No Concerns Found</div>
            <div style="font-size:0.85em; color:#0f6e56; line-height:1.6;">Our current data sources did not flag specific concerns for ${labels[communityId]} communities at ${businessName}. This does not guarantee no issues exist.</div>
        </div>`}
        <div style="font-size:0.75em; font-weight:700; text-transform:uppercase; letter-spacing:1px; color:var(--blue-muted); margin-bottom:8px; margin-top:14px;">About This Community</div>
        <div style="font-size:0.85em; color:#4a5166; line-height:1.7; margin-bottom:14px;">${info ? info.description : 'We track discrimination concerns, legal cases, and policy impacts for this community.'}</div>
        <a href="${sourceLinks[communityId].url}" target="_blank" style="display:inline-block; padding:10px 18px; background:var(--blue); color:white; border-radius:8px; font-size:0.88em; font-weight:600; text-decoration:none;">${sourceLinks[communityId].label} →</a>
    `;

    document.getElementById('drawerOverlay').classList.add('open');
    document.getElementById('drawer').classList.add('open');
}

// ===== INFO DRAWER =====
function openInfoDrawer(type) {
    document.getElementById('drawerScoreSection').innerHTML = '';
    document.getElementById('drawerActions').innerHTML = '';

    if (type === 'companies') {
        document.getElementById('drawerTitle').textContent = 'Companies Tracked';
        document.getElementById('drawerVerdict').textContent = `${ALL_COMPANIES.length} companies in our database`;
        document.getElementById('drawerBody').innerHTML = `
            <input class="search-filter" id="companyFilter" placeholder="Search companies..." oninput="filterCompanies()" />
            <div id="companyList">
                ${ALL_COMPANIES.map(c => `
                    <div class="info-item" onclick="closeDrawer(); quickBusinessSearch('${c.replace(/'/g, "\\'")}')">
                        <div class="info-item-name">${c}</div>
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m9 18 6-6-6-6"/></svg>
                    </div>`).join('')}
            </div>
            <div style="margin-top:16px; padding-top:14px; border-top:1px solid var(--navy-100);">
                <p style="font-size:0.82em; color:var(--blue-muted); margin-bottom:10px;">Don't see your company? Submit it for review.</p>
                <button class="btn-outline" onclick="openInfoDrawer('submit')">Submit a Company</button>
            </div>`;
            
    } else if (type === 'more-categories') {
        document.getElementById('drawerTitle').textContent = 'More Stop Categories';
        document.getElementById('drawerVerdict').textContent = 'Add to your safe stop search';
        document.getElementById('drawerBody').innerHTML = `
            <p style="font-size:0.85em; color:#4a5166; margin-bottom:16px; line-height:1.6;">Select additional categories to include in your safe stop recommendations.</p>
            <div style="display:flex; flex-direction:column; gap:8px;">
                ${[
                    {cat:'lgbtq', label:'LGBTQ+ Spaces', desc:'Queer-owned and affirming businesses'},
                    {cat:'black_owned', label:'Black-Owned', desc:'Verified via ByBlack and Black Owned API'},
                    {cat:'women_owned', label:'Women-Owned', desc:'WBENC certified businesses'},
                    {cat:'accessible', label:'Fully Accessible', desc:'Wheelchair accessible entrance, restroom, and seating'},
                    {cat:'pharmacy', label:'Pharmacy', desc:'CVS, Walgreens, and independent pharmacies'},
                    {cat:'coffee', label:'Coffee', desc:'Cafes and coffee shops'}
                ].map(c => `
                    <div style="background:var(--gray-100); border-radius:8px; padding:12px 14px; display:flex; align-items:center; justify-content:space-between; cursor:pointer;" onclick="addCategory('${c.cat}', '${c.label}')">
                        <div>
                            <div style="font-size:0.88em; font-weight:600; color:#0a1628;">${c.label}</div>
                            <div style="font-size:0.78em; color:var(--blue-muted); margin-top:2px;">${c.desc}</div>
                        </div>
                        <button class="btn-outline" style="font-size:0.75em; padding:5px 10px;">Add</button>
                    </div>`).join('')}
            </div>`;
        document.getElementById('drawerOverlay').classList.add('open');
        document.getElementById('drawer').classList.add('open');        
            
    } else if (type === 'states') {
        document.getElementById('drawerTitle').textContent = 'States Covered';
        document.getElementById('drawerVerdict').textContent = 'All 50 states + Washington DC';
        const states = ['Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut','Delaware','Florida','Georgia','Hawaii','Idaho','Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana','Maine','Maryland','Massachusetts','Michigan','Minnesota','Mississippi','Missouri','Montana','Nebraska','Nevada','New Hampshire','New Jersey','New Mexico','New York','North Carolina','North Dakota','Ohio','Oklahoma','Oregon','Pennsylvania','Rhode Island','South Carolina','South Dakota','Tennessee','Texas','Utah','Vermont','Virginia','Washington','West Virginia','Wisconsin','Wyoming','Washington DC'];
        document.getElementById('drawerBody').innerHTML = `
            <input class="search-filter" id="stateFilter" placeholder="Search states..." oninput="filterStates()" />
            <div id="stateList">
                ${states.map(s => `
                    <div class="info-item" onclick="closeDrawer(); switchPanel('travel'); quickSearch('${s}')">
                        <div class="info-item-name">${s}</div>
                        <span class="badge ${HIGH_RISK_STATES.includes(s) ? 'badge-high' : 'badge-low'}">${HIGH_RISK_STATES.includes(s) ? 'High Risk' : 'Low Risk'}</span>
                    </div>`).join('')}
            </div>`;
    } else if (type === 'sources') {
        document.getElementById('drawerTitle').textContent = 'Data Sources';
        document.getElementById('drawerVerdict').textContent = `${Object.keys(DATA_SOURCES).length} independent data sources`;
        document.getElementById('drawerBody').innerHTML = Object.entries(DATA_SOURCES).map(([key, source]) => `
            <div style="margin-bottom:16px; padding-bottom:16px; border-bottom:1px solid var(--navy-100);">
                <div style="font-weight:600; font-size:0.92em; color:#0a1628; margin-bottom:4px;">${source.title}</div>
                <div style="font-size:0.82em; color:#4a5166; line-height:1.6; margin-bottom:6px;">${source.description}</div>
                <div style="font-size:0.78em; color:var(--coral-600); font-weight:600;">${source.impact}</div>
                <a href="${source.url}" target="_blank" style="font-size:0.78em; color:var(--blue-muted); display:inline-block; margin-top:4px;">${source.url} →</a>
            </div>`).join('');
    } else if (type === 'communities') {
        document.getElementById('drawerTitle').textContent = 'Communities Protected';
        document.getElementById('drawerVerdict').textContent = '5 marginalized communities tracked';
        document.getElementById('drawerBody').innerHTML = Object.values(COMMUNITIES_INFO).map(c => `
            <div style="margin-bottom:16px; padding-bottom:16px; border-bottom:1px solid var(--navy-100);">
                <div style="font-weight:600; font-size:0.92em; color:#0a1628; margin-bottom:6px;">${c.label}</div>
                <div style="font-size:0.82em; color:#4a5166; line-height:1.6;">${c.description}</div>
            </div>`).join('');
    } else if (type === 'submit') {
        document.getElementById('drawerTitle').textContent = 'Submit a Company';
        document.getElementById('drawerVerdict').textContent = 'Help us expand our database';
        document.getElementById('drawerBody').innerHTML = `
            <p style="font-size:0.85em; color:#4a5166; margin-bottom:16px; line-height:1.6;">Submit a company for review and we'll research and add it to our transparency database.</p>
            <div class="submit-form">
                <div><label>Company Name *</label><input type="text" id="submitName" placeholder="e.g. Trader Joe's" /></div>
                <div><label>Category *</label>
                    <select id="submitCategory">
                        <option value="">Select a category...</option>
                        <option>Retail / Shopping</option>
                        <option>Fast Food / Restaurant</option>
                        <option>Technology</option>
                        <option>Banking / Finance</option>
                        <option>Healthcare / Pharma</option>
                        <option>Energy / Oil</option>
                        <option>Food & Beverage</option>
                        <option>Insurance</option>
                        <option>Telecom</option>
                        <option>Automotive</option>
                        <option>Travel / Hospitality</option>
                        <option>Education</option>
                        <option>Law Enforcement</option>
                        <option>Other</option>
                    </select>
                </div>
                <div><label>Company Website</label><input type="text" id="submitWebsite" placeholder="e.g. https://traderjoes.com" /></div>
                <div><label>Additional Notes</label><textarea id="submitNotes" placeholder="Any known ESG concerns, labor practices, or other relevant information..."></textarea></div>
                <button class="btn-primary" onclick="submitCompany()">Submit for Review</button>
                <div id="submitResult"></div>
            </div>`;
    } else if (type.startsWith('source-')) {
        const source = DATA_SOURCES[type];
        if (source) {
            document.getElementById('drawerTitle').textContent = source.title;
            document.getElementById('drawerVerdict').textContent = 'Data Source Methodology';
            document.getElementById('drawerBody').innerHTML = `
                <div style="font-size:0.9em; color:#4a5166; line-height:1.7; margin-bottom:14px;">${source.description}</div>
                <div style="background:var(--coral-100); padding:12px; border-radius:8px; margin-bottom:14px;">
                    <div style="font-size:0.75em; font-weight:600; text-transform:uppercase; letter-spacing:1px; color:#8a2020; margin-bottom:4px;">Score Impact</div>
                    <div style="font-size:0.88em; color:#8a2020;">${source.impact}</div>
                </div>
                <a href="${source.url}" target="_blank" style="display:inline-block; padding:10px 18px; background:var(--blue); color:white; border-radius:8px; font-size:0.88em; font-weight:600; text-decoration:none;">Visit ${source.title} →</a>`;
        }
    }

    document.getElementById('drawerOverlay').classList.add('open');
    document.getElementById('drawer').classList.add('open');
}

function addCategory(cat, label) {
    const bar = document.querySelector('.cat-pill.more').parentElement;
    if (!bar.querySelector(`[data-cat="${cat}"]`)) {
        const pill = document.createElement('button');
        pill.className = 'cat-pill active';
        pill.dataset.cat = cat;
        pill.textContent = label;
        pill.onclick = function() { toggleCat(this); };
        bar.insertBefore(pill, bar.querySelector('.cat-pill.more'));
    }
    closeDrawer();
}

function filterCompanies() {
    const filter = document.getElementById('companyFilter').value.toLowerCase();
    document.querySelectorAll('#companyList .info-item').forEach(item => {
        item.style.display = item.textContent.toLowerCase().includes(filter) ? 'flex' : 'none';
    });
}

function filterStates() {
    const filter = document.getElementById('stateFilter').value.toLowerCase();
    document.querySelectorAll('#stateList .info-item').forEach(item => {
        item.style.display = item.textContent.toLowerCase().includes(filter) ? 'flex' : 'none';
    });
}

async function submitCompany() {
    const name = document.getElementById('submitName').value.trim();
    const category = document.getElementById('submitCategory').value;
    const website = document.getElementById('submitWebsite').value.trim();
    const notes = document.getElementById('submitNotes').value.trim();
    const resultDiv = document.getElementById('submitResult');
    if (!name || !category) { resultDiv.innerHTML = `<div class="error-msg" style="margin-top:10px;">Please enter a company name and select a category.</div>`; return; }
    try {
        const response = await fetch(`/submit_company?company_name=${encodeURIComponent(name)}&category=${encodeURIComponent(category)}&website=${encodeURIComponent(website)}&notes=${encodeURIComponent(notes)}`, { method: 'POST' });
        const data = await response.json();
        if (data.success) {
            resultDiv.innerHTML = `<div class="success-msg" style="margin-top:10px;">${data.message}</div>`;
            document.getElementById('submitName').value = '';
            document.getElementById('submitCategory').value = '';
            document.getElementById('submitWebsite').value = '';
            document.getElementById('submitNotes').value = '';
        } else {
            resultDiv.innerHTML = `<div class="error-msg" style="margin-top:10px;">${data.message}</div>`;
        }
    } catch (e) {
        resultDiv.innerHTML = `<div class="error-msg" style="margin-top:10px;">Could not submit. Please try again.</div>`;
    }
}

// ===== BUSINESS DRAWER =====
function openBusinessDrawer(businessName, data) {
    const sc = getScoreClass(data.score);
    document.getElementById('drawerTitle').textContent = data.business;
    document.getElementById('drawerVerdict').textContent = getVerdict(data.score);
    document.getElementById('drawerScoreSection').innerHTML = `
        <div class="drawer-score">
            <div class="drawer-score-circle ${sc}">
                <div class="drawer-score-num ${sc}">${data.score}</div>
                <div class="score-out">/100</div>
            </div>
            <div style="font-size:0.85em; color:#4a5166; line-height:1.6;">${data.summary}</div>
        </div>`;
    const flagsHtml = data.flags && data.flags.length > 0
        ? data.flags.map(f => renderFlag(f)).join('')
        : '<p style="color:var(--blue-muted); font-size:0.85em;">No major flags detected.</p>';
    const altHtml = data.alternatives && data.alternatives.length > 0
        ? `<div class="drawer-section-title">Ethical Alternatives</div>
           ${data.alternatives.map(a => `<div class="biz-row" onclick="closeDrawer(); quickBusinessSearch('${a.name}')"><div><div class="biz-name">${a.name}</div><div class="biz-sub">ESG: ${a.esg_rating}</div></div><span class="badge badge-low">${a.score}/100</span></div>`).join('')}`
        : '';
    document.getElementById('drawerBody').innerHTML = `
        <div class="drawer-section-title">Flags & Concerns</div>
        ${flagsHtml}
        ${altHtml}`;
    document.getElementById('drawerActions').innerHTML = `
        <button class="btn-primary" onclick="findNearestAndRoute('${businessName}')">Find Nearest</button>
        <button class="btn-secondary" onclick="checkAreaSafety('${businessName}')">Area Safety</button>
        <button class="btn-outline-navy" onclick="window.open('https://www.google.com/maps/search/${encodeURIComponent(businessName)}','_blank')">Maps</button>`;
    document.getElementById('drawerOverlay').classList.add('open');
    document.getElementById('drawer').classList.add('open');
}

function renderFlag(flag) {
    if (flag.startsWith('HEADLINE|')) {
        const parts = flag.split('|');
        const title = parts[1] || '';
        const url = parts[2] || '';
        const source = parts[3] || '';
        return `<div class="flag-item"><div class="flag-dot"></div><div>${title}${url ? `<a href="${url}" target="_blank" class="flag-link">${source || 'Read More'} →</a>` : ''}</div></div>`;
    }
    return `<div class="flag-item"><div class="flag-dot"></div>${flag}</div>`;
}

function closeDrawer() {
    document.getElementById('drawerOverlay').classList.remove('open');
    document.getElementById('drawer').classList.remove('open');
}

function prefillRoute(businessName) { closeDrawer(); switchPanel('route'); document.getElementById('routeDestination').value = businessName; document.getElementById('routeOrigin').focus(); }
function checkAreaSafety(businessName) { closeDrawer(); switchPanel('travel'); document.getElementById('travelInput').value = businessName; searchTravel(); }
function prefillRouteToLocation(location) { switchPanel('route'); document.getElementById('routeDestination').value = location; document.getElementById('routeOrigin').focus(); }

async function findNearestAndRoute(businessName) {
    if (!navigator.geolocation) { closeDrawer(); switchPanel('route'); document.getElementById('routeDestination').value = businessName; return; }
    navigator.geolocation.getCurrentPosition(async position => {
        const { latitude: lat, longitude: lon } = position.coords;
        try {
            const response = await fetch(`/nearest_location?business_name=${encodeURIComponent(businessName)}&lat=${lat}&lon=${lon}`, { method: 'POST' });
            const data = await response.json();
            closeDrawer(); switchPanel('route');
            document.getElementById('routeDestination').value = data.found ? `${data.name}, ${data.address}` : businessName;
            document.getElementById('routeOrigin').focus();
        } catch (e) { closeDrawer(); switchPanel('route'); document.getElementById('routeDestination').value = businessName; }
    }, () => { closeDrawer(); switchPanel('route'); document.getElementById('routeDestination').value = businessName; });
}

// ===== HELPERS =====
function getBadgeClass(rating) {
    if (!rating) return '';
    const r = rating.toLowerCase();
    if (r.includes('low') || r.includes('negligible')) return 'badge-low';
    if (r.includes('medium')) return 'badge-medium';
    if (r.includes('severe')) return 'badge-severe';
    if (r.includes('high')) return 'badge-high';
    return 'badge-medium';
}

function getBannerClass(overall) {
    if (!overall) return '';
    const r = overall.toLowerCase();
    if (r.includes('low')) return 'banner-low';
    if (r.includes('medium')) return 'banner-medium';
    return 'banner-high';
}

function getScoreClass(score) {
    if (score >= 75) return 'high';
    if (score >= 50) return 'medium';
    return 'low';
}

function getVerdict(score) {
    if (score >= 75) return 'Good Transparency';
    if (score >= 50) return 'Moderate Transparency';
    return 'Poor Transparency';
}

function checkSafetyAlert(location) {
    const alertDiv = document.getElementById('safety-alert');
    if (!alertDiv) return;
    const matched = HIGH_RISK_STATES.find(state => location.toUpperCase().includes(state.toUpperCase()));
    if (matched) { alertDiv.textContent = `Safety Advisory: ${matched} has active travel advisories for marginalized communities. Review the safety ratings below carefully.`; alertDiv.classList.add('visible'); }
    else { alertDiv.classList.remove('visible'); }
}

function showLoadingSpinner(divId) {
    const el = document.getElementById(divId);
    if (el) el.innerHTML = `<div class="loading"><div class="loading-spinner"></div>Searching...</div>`;
}

// ===== BUSINESS SEARCH =====
let lastBusinessData = null;

async function searchBusiness() {
    const name = document.getElementById('searchInput').value.trim();
    if (!name) return;
    showLoadingSpinner('results');
    try {
        const response = await fetch(`/search?business_name=${encodeURIComponent(name)}`, { method: 'POST' });
        const data = await response.json();
        lastBusinessData = data;
        displayResults(data);
    } catch (e) {
        document.getElementById('results').innerHTML = `<div class="error-msg">Could not connect to the API.</div>`;
    }
}

function quickBusinessSearch(name) {
    document.getElementById('searchInput').value = name;
    switchPanel('business');
    window.scrollTo(0, 0);
    searchBusiness();
}

function displayResults(data) {
    const sc = getScoreClass(data.score);
    // Show product redirect notice if applicable
    const productNote = data.product_redirect && data.product_redirect.found
        ? `<div style="background:var(--teal-faint); border:1px solid var(--teal); border-radius:8px; padding:10px 14px; margin-bottom:12px; font-size:0.85em; color:#085041;">
            <strong>${data.product_redirect.searched_product}</strong> is a product of <strong>${data.product_redirect.parent_company}</strong> — showing company transparency score.
           </div>`
        : '';
    const circumference = 2 * Math.PI * 40;
    const progress = (data.score / 100) * circumference;

    const legal = data.legal_data || {};
    const esg = data.esg_data || {};
    const hr = data.human_rights_data || {};
    const reviews = data.google_reviews || {};

    const altHtml = data.alternatives && data.alternatives.length > 0
        ? `<div class="card"><h4>Ethical Alternatives in Same Category</h4>
           ${data.alternatives.map(a => `<div class="biz-row" onclick="quickBusinessSearch('${a.name}')"><div><div class="biz-name">${a.name}</div><div class="biz-sub">ESG: ${a.esg_rating}</div></div><span class="badge badge-low">${a.score}/100</span></div>`).join('')}</div>`
        : '';

const corpwatch = data.corpwatch_data || {};
    const corpwatchHtml = corpwatch.found ? `
        <div class="card">
            <h4>Corporate Structure</h4>
            <div style="display:flex; flex-wrap:wrap; gap:8px; margin-bottom:10px;">
                ${corpwatch.parent_company ? `<div class="metric-card" style="flex:1;"><div class="metric-num ok" style="font-size:1em;">${corpwatch.parent_company}</div><div class="metric-label">Parent Company</div></div>` : ''}
                ${corpwatch.subsidiary_count > 0 ? `<div class="metric-card" style="flex:1;"><div class="metric-num">${corpwatch.subsidiary_count}</div><div class="metric-label">Subsidiaries</div></div>` : ''}
                ${corpwatch.country_count > 0 ? `<div class="metric-card" style="flex:1;"><div class="metric-num ok">${corpwatch.country_count}</div><div class="metric-label">Countries</div></div>` : ''}
            </div>
            ${corpwatch.industry ? `<p style="font-size:0.82em; color:var(--blue-muted); margin-bottom:6px;">Industry: ${corpwatch.industry}</p>` : ''}
            ${corpwatch.countries && corpwatch.countries.length > 0 ? `<p style="font-size:0.82em; color:var(--blue-muted);">Operating in: ${corpwatch.countries.join(', ')}</p>` : ''}
            ${corpwatch.source_url ? `<a href="${corpwatch.source_url}" target="_blank" style="font-size:0.78em; color:var(--teal); font-weight:600; margin-top:8px; display:inline-block;">Full corporate profile →</a>` : ''}
        </div>` : '';

    document.getElementById('results').innerHTML = `
        ${productNote}
        <div class="score-hero">
            <div class="ring-wrap">
                <svg viewBox="0 0 88 88">
                    <circle class="ring-track" cx="44" cy="44" r="40"/>
                    <circle id="ringFill" class="ring-fill ${sc}" cx="44" cy="44" r="40"
                        stroke-dasharray="0 ${circumference}"
                        stroke-dashoffset="0"/>
                </svg>
                <div class="ring-center">
                    <div class="ring-score ${sc}">${data.score}</div>
                    <div class="ring-out">/100</div>
                </div>
            </div>
            <div class="score-info">
                <h3>${data.business}</h3>
                <div class="verdict ${sc}">${getVerdict(data.score)}</div>
                <div class="score-summary">${data.summary}</div>
                <div class="score-actions">
                    <button class="btn-outline" onclick="openBusinessDrawer('${data.business}', lastBusinessData)">Full Details</button>
                    <button class="btn-outline" onclick="findNearestAndRoute('${data.business}')">Find & Route</button>
                    <button class="btn-outline" onclick="checkAreaSafety('${data.business}')">Area Safety</button>
                </div>
            </div>
        </div>

        <div class="metrics-row">
            <div class="metric-card">
                <div class="metric-num ${legal.found && legal.case_count > 0 ? '' : 'ok'}">${legal.found ? legal.case_count || 0 : 0}</div>
                <div class="metric-label">Court Cases</div>
            </div>
            <div class="metric-card">
                <div class="metric-num ${esg.found && esg.score_impact > 10 ? '' : 'ok'}">${esg.found ? esg.rating || 'N/A' : 'N/A'}</div>
                <div class="metric-label">ESG Risk</div>
            </div>
            <div class="metric-card">
                <div class="metric-num ${reviews && reviews.found && reviews.rating < 3.5 ? '' : 'ok'}">${reviews && reviews.found && reviews.rating ? reviews.rating + '★' : 'N/A'}</div>
                <div class="metric-label">Google Rating</div>
            </div>
        </div>

        ${renderCommunityFlags(data)}

        <div class="card">
            <h4>Flags & Concerns</h4>
            ${data.flags && data.flags.length > 0 ? data.flags.map(f => renderFlag(f)).join('') : '<p style="color:var(--blue-muted); font-size:0.85em;">No major flags detected.</p>'}
            ${data.nlrb_data && data.nlrb_data.found ? `
            <div style="margin-top:10px; padding-top:10px; border-top:1px solid var(--navy-100);">
                <div style="font-size:0.7em; font-weight:700; text-transform:uppercase; letter-spacing:1px; color:var(--blue-muted); margin-bottom:6px;">NLRB Labor Record</div>
                <div class="flag-item"><div class="flag-dot"></div>${data.nlrb_data.case_count} unfair labor practice charges filed — ${data.nlrb_data.summary}</div>
                ${data.nlrb_data.sources ? data.nlrb_data.sources.map(s => `<a href="${s.url}" target="_blank" style="display:inline-block; font-size:0.78em; font-weight:600; color:var(--teal); padding:3px 8px; background:var(--teal-faint); border-radius:4px; margin:3px 3px 0 0; text-decoration:none;">${s.label} →</a>`).join('') : ''}
            </div>` : ''}
        </div>

        ${altHtml}
        ${corpwatchHtml}
    `;

    animateRing(data.score);
}

document.getElementById('searchInput').addEventListener('keypress', e => { if (e.key === 'Enter') searchBusiness(); });

// ===== TRAVEL =====
async function searchTravel() {
    const location = document.getElementById('travelInput').value.trim();
    if (!location) return;
    checkSafetyAlert(location);
    showLoadingSpinner('travel-results');
    try {
        const [travelRes, localRes] = await Promise.all([
            fetch(`/travel_by_address?address=${encodeURIComponent(location)}`, { method: 'POST' }),
            fetch(`/local?location=${encodeURIComponent(location)}`, { method: 'POST' })
        ]);
        const travelData = await travelRes.json();
        const localData = await localRes.json();
        displayTravelResults(travelData, localData);
        window.scrollTo(0, 0);
    } catch (e) {
        document.getElementById('travel-results').innerHTML = `<div class="error-msg">Could not connect to the API.</div>`;
    }
}

function quickSearch(state) { document.getElementById('travelInput').value = state; checkSafetyAlert(state); searchTravel(); }

function renderSafetyItem(label, data, mapData) {
    if (!data) return '';
    const advisories = data.advisories && data.advisories.length > 0 ? data.advisories.map(a => `<div class="advisory">${a}</div>`).join('') : '';
    const mapDetails = (label === 'LGBTQ+ Safety' && mapData) ? `
        <div style="margin-top:6px; display:flex; flex-wrap:wrap; gap:4px;">
            ${mapData.nondiscrimination_law !== undefined ? `<span class="badge ${mapData.nondiscrimination_law ? 'badge-low' : 'badge-high'}" style="font-size:0.68em;">Nondiscrimination law: ${mapData.nondiscrimination_law ? 'Yes' : 'No'}</span>` : ''}
            ${mapData.conversion_therapy_ban !== undefined ? `<span class="badge ${mapData.conversion_therapy_ban ? 'badge-low' : 'badge-high'}" style="font-size:0.68em;">Conversion therapy ban: ${mapData.conversion_therapy_ban ? 'Yes' : 'No'}</span>` : ''}
            ${mapData.anti_trans_laws !== undefined ? `<span class="badge ${mapData.anti_trans_laws ? 'badge-high' : 'badge-low'}" style="font-size:0.68em;">Anti-trans laws: ${mapData.anti_trans_laws ? 'Yes' : 'No'}</span>` : ''}
            ${mapData.map_score !== undefined ? `<span class="badge badge-unrated" style="font-size:0.68em;">MAP score: ${mapData.map_score}</span>` : ''}
            ${mapData.map_source ? `<a href="${mapData.map_source}" target="_blank" style="font-size:0.68em; color:var(--teal); font-weight:600; padding:2px 6px; background:var(--teal-faint); border-radius:4px;">Full MAP profile →</a>` : ''}
        </div>` : '';
    return `<div class="safety-item"><h5>${label} <span class="badge ${getBadgeClass(data.rating)}">${data.rating}</span></h5><p>${data.notes}</p>${advisories}${mapDetails}</div>`;
}

function renderPoliceViolence(policeData) {
    if (!policeData) return '';
    const state = policeData.state;
    const city = policeData.city;
    if ((!state || !state.found) && (!city || !city.found)) return '';
    let html = `<div class="section-divider">Police Violence Data</div>`;
    if (city && city.found) {
        const breakdown = city.racial_breakdown ? Object.entries(city.racial_breakdown).map(([r, c]) => `<div class="advisory">${r}: ${c} incidents</div>`).join('') : '';
        html += `<div class="safety-item"><h5>City Level <span class="badge ${getBadgeClass(city.risk_level)}">${city.risk_level}</span></h5><p>Total: ${city.total_incidents} · Accountability: ${city.accountability_rate} · Unarmed: ${city.unarmed_rate}</p>${breakdown}</div>`;
    }
    if (state && state.found) {
        const breakdown = state.racial_breakdown ? Object.entries(state.racial_breakdown).slice(0,5).map(([r, c]) => `<div class="advisory">${r}: ${c} incidents</div>`).join('') : '';
        html += `<div class="safety-item"><h5>State Level <span class="badge ${getBadgeClass(state.risk_level)}">${state.risk_level}</span></h5><p>Total: ${state.total_incidents} · Accountability: ${state.accountability_rate} · Unarmed: ${state.unarmed_rate} · Body cam: ${state.body_camera_rate}</p>${breakdown}</div>`;
    }
    return html;
}

function displayTravelResults(data, localData) {
    const resultsDiv = document.getElementById('travel-results');
    if (!data.found) { resultsDiv.innerHTML = `<div class="error-msg">${data.message}</div>`; return; }
    const nearbyHtml = localData && localData.found && localData.nearby_scored && localData.nearby_scored.length > 0
        ? localData.nearby_scored.map(b => `<div class="biz-row" onclick="quickBusinessSearch('${b.name}')"><div><div class="biz-name">${b.name}</div><div class="biz-sub">${b.address || ''}</div><div class="biz-sub">${b.distance_miles != null ? b.distance_miles + ' mi · ' : ''}ESG: ${b.esg_rating} · HR: ${b.hr_rating}</div></div><span class="badge ${getBadgeClass(b.score >= 75 ? 'low' : b.score >= 50 ? 'medium' : 'high')}">${b.score}/100</span></div>`).join('')
        : '<p style="color:var(--blue-muted); font-size:0.85em;">No scored businesses found nearby.</p>';
    const unratedHtml = localData && localData.found && localData.nearby_unrated && localData.nearby_unrated.length > 0
        ? localData.nearby_unrated.map(b => `<div class="biz-row"><div><div class="biz-name">${b.name}</div><div class="biz-sub">${b.address || ''}${b.distance_miles != null ? ' · ' + b.distance_miles + ' mi' : ''}</div></div><span class="badge badge-unrated">Unrated</span></div>`).join('') : '';
    const altHtml = localData && localData.found && localData.ethical_alternatives && localData.ethical_alternatives.length > 0
        ? localData.ethical_alternatives.map(b => `<div class="biz-row" onclick="quickBusinessSearch('${b.name}')"><div><div class="biz-name">${b.name}</div><div class="biz-sub">ESG: ${b.esg_rating}</div></div><span class="badge badge-low">${b.score}/100</span></div>`).join('') : '';
    resultsDiv.innerHTML = `
        <div class="${getBannerClass(data.overall_rating)} overall-banner"><span>${data.location}</span><span>Overall: ${data.overall_rating}</span></div>
        <button class="btn-outline" onclick="prefillRouteToLocation('${data.location}')" style="margin-bottom:12px;">Plan Safe Route Here</button>
        <div class="safety-grid">
            ${renderSafetyItem('LGBTQ+ Safety', data.lgbtq, data.map_data)}
        ${renderSafetyItem('Racial Safety', data.racial, null)}
        ${renderSafetyItem('Religious Minority', data.religious_minority, null)}
        ${renderSafetyItem('Disability Access', data.disability, null)}
        ${renderSafetyItem("Women's Safety", data.women, null)}
        </div>
        ${renderPoliceViolence(data.police_violence)}
        <div class="section-divider">Nearby Businesses</div>
        ${nearbyHtml}
        ${unratedHtml ? `<div class="section-divider">Other Nearby (Unrated)</div>${unratedHtml}` : ''}
        ${altHtml ? `<div class="section-divider">Ethical Alternatives</div>${altHtml}` : ''}`;
}

document.getElementById('travelInput').addEventListener('keypress', e => { if (e.key === 'Enter') searchTravel(); });

// ===== GPS =====
function getLocation() {
    if (!navigator.geolocation) { document.getElementById('location-status').textContent = 'Geolocation not supported.'; return; }
    document.getElementById('location-status').textContent = 'Detecting your location...';
    navigator.geolocation.getCurrentPosition(
        position => reverseGeocode(position.coords.latitude, position.coords.longitude),
        () => { document.getElementById('location-status').textContent = 'Location access denied. Please search manually.'; }
    );
}

async function reverseGeocode(lat, lon) {
    try {
        document.getElementById('location-status').textContent = 'Finding your location...';
        showLoadingSpinner('travel-results');
        const [travelRes, localRes] = await Promise.all([
            fetch(`/travel_by_address?address=${encodeURIComponent(lat + ',' + lon)}`, { method: 'POST' }),
            fetch(`/local_by_coords?lat=${lat}&lon=${lon}`, { method: 'POST' })
        ]);
        const travelData = await travelRes.json();
        const localData = await localRes.json();
        if (travelData.found) { document.getElementById('travelInput').value = travelData.location; document.getElementById('location-status').textContent = `Location detected: ${travelData.location}`; checkSafetyAlert(travelData.location); }
        else { document.getElementById('location-status').textContent = 'Could not determine location. Please search manually.'; }
        displayTravelResults(travelData, localData);
    } catch (e) { document.getElementById('location-status').textContent = 'Could not detect location. Please search manually.'; }
}

// ===== TRACKING =====
let trackingInterval = null;
let lastTrackedState = null;

function startTracking() {
    if (!navigator.geolocation) { alert('Geolocation not supported.'); return; }
    document.getElementById('tracking-btn').style.display = 'none';
    document.getElementById('tracking-bar').classList.add('active');
    document.getElementById('tracking-status').textContent = 'Getting your location...';
    switchPanel('travel');
    checkCurrentLocation();
    trackingInterval = setInterval(checkCurrentLocation, 30000);
}

function stopTracking() {
    if (trackingInterval) { clearInterval(trackingInterval); trackingInterval = null; }
    lastTrackedState = null;
    document.getElementById('tracking-btn').style.display = 'block';
    document.getElementById('tracking-bar').classList.remove('active');
}

function checkCurrentLocation() {
    navigator.geolocation.getCurrentPosition(async position => {
        const { latitude: lat, longitude: lon } = position.coords;
        try {
            const response = await fetch(`/travel_by_address?address=${encodeURIComponent(lat + ',' + lon)}`, { method: 'POST' });
            const data = await response.json();
            if (data.found) {
                const parts = data.location.split(',');
                const currentState = parts[parts.length - 2]?.trim() || parts[parts.length - 1]?.trim();
                document.getElementById('tracking-status').textContent = `Tracking: ${data.location}`;
                if (currentState !== lastTrackedState) {
                    lastTrackedState = currentState;
                    checkSafetyAlert(data.location);
                    const isHighRisk = HIGH_RISK_STATES.some(s => data.location.toUpperCase().includes(s.toUpperCase()));
                    showTrackingNotification(isHighRisk ? `Entered ${currentState} — High Risk state. Review safety ratings.` : `Entered ${currentState}.`, isHighRisk);
                    const localRes = await fetch(`/local_by_coords?lat=${lat}&lon=${lon}`, { method: 'POST' });
                    const localData = await localRes.json();
                    displayTravelResults(data, localData);
                }
            }
        } catch (e) { document.getElementById('tracking-status').textContent = 'Could not update location.'; }
    }, () => { stopTracking(); });
}

function showTrackingNotification(message, isHighRisk) {
    const n = document.createElement('div');
    n.className = 'notification';
    n.style.background = isHighRisk ? 'var(--coral-600)' : 'var(--teal)';
    n.textContent = message;
    document.body.appendChild(n);
    setTimeout(() => { n.style.opacity = '0'; setTimeout(() => n.remove(), 500); }, 5000);
}

// ===== ROUTE =====
async function planRoute(withDirections) {
    const origin = document.getElementById('routeOrigin').value.trim();
    const destination = document.getElementById('routeDestination').value.trim();
    if (!origin || !destination) return;
    showLoadingSpinner('route-results');
    const mapContainer = document.getElementById('map-container');
    const mapIframe = document.getElementById('map-iframe');
    const GOOGLE_KEY = 'AIzaSyBalxLq35w_7SCawNXOq-xpzpd06cWUpyM';
    mapIframe.src = `https://www.google.com/maps/embed/v1/directions?key=${GOOGLE_KEY}&origin=${encodeURIComponent(origin)}&destination=${encodeURIComponent(destination)}&mode=driving`;
    mapContainer.style.display = 'block';
    try {
        const response = await fetch(`/route_safety?origin=${encodeURIComponent(origin)}&destination=${encodeURIComponent(destination)}`, { method: 'POST' });
        const data = await response.json();
        displayRouteResults(data, withDirections);
        showDriveInterval();
        setTimeout(() => fetchSafeStops(), 300);
    } catch (e) {
        document.getElementById('route-results').innerHTML = `<div class="error-msg">Could not plan route. Please try again.</div>`;
    }
}

async function fetchSafeStops() {
    const origin = document.getElementById('routeOrigin').value.trim();
    const destination = document.getElementById('routeDestination').value.trim();
    const intervalHours = document.getElementById('intervalCustom')?.value || document.querySelector('.drive-opt.selected')?.dataset.hours || 4;
    const categories = getSelectedCategories();
    if (!origin || !destination) return;

    document.getElementById('safe-stops-section').innerHTML = `<div class="loading"><div class="loading-spinner"></div>Finding safe stops...</div>`;

    try {
        const response = await fetch(
            `/route_safe_stops?origin=${encodeURIComponent(origin)}&destination=${encodeURIComponent(destination)}&interval_hours=${intervalHours}&categories=${encodeURIComponent(categories)}`,
            { method: 'POST' }
        );
        const data = await response.json();
        displaySafeStops(data);
    } catch (e) {
        document.getElementById('safe-stops-section').innerHTML = `<div class="error-msg">Could not load safe stops.</div>`;
    }
}

function getRouteStateClass(overall) {
    if (!overall) return '';
    const r = overall.toLowerCase();
    if (r.includes('low')) return 'low-risk';
    if (r.includes('medium')) return 'medium-risk';
    return 'high-risk';
}

function displayRouteResults(data, withDirections) {
    const resultsDiv = document.getElementById('route-results');
    if (!data.found) { resultsDiv.innerHTML = `<div class="error-msg">${data.message}</div>`; return; }
    const highRiskColor = data.high_risk_states > 0 ? 'var(--coral-400)' : 'var(--teal-light)';
    const statesHtml = data.states_on_route.map(state => `
        <div class="route-state ${getRouteStateClass(state.overall)}">
            <div class="route-state-header">
                <div class="route-state-name">${state.state}</div>
                <div style="display:flex; gap:6px; align-items:center;">
                    <span class="badge ${getBadgeClass(state.overall)}">${state.overall}</span>
                    <button class="btn-outline-navy" style="padding:4px 8px; font-size:0.72em;" onclick="quickSearch('${state.state}')">Details</button>
                    <button class="btn-outline-navy" style="padding:4px 8px; font-size:0.72em; border-color:var(--teal); color:var(--teal);" onclick="fetchStateStops('${state.state}')">Stops</button>
                </div>
            </div>
            <div class="route-state-ratings">
                <span class="badge ${getBadgeClass(state.lgbtq)}" style="font-size:0.7em;">LGBTQ+: ${state.lgbtq}</span>
                <span class="badge ${getBadgeClass(state.racial)}" style="font-size:0.7em;">Racial: ${state.racial}</span>
                <span class="badge ${getBadgeClass(state.women)}" style="font-size:0.7em;">Women: ${state.women}</span>
            </div>
            ${state.advisories && state.advisories.length > 0 ? `<div class="advisory" style="margin-top:8px;">${state.advisories[0]}</div>` : ''}
        </div>`).join('');

    let directionsHtml = '';
    if (withDirections && data.directions && data.directions.length > 0) {
        let stepCount = 0;
        directionsHtml = `<div class="section-divider">Turn-by-Turn Directions</div>
            <div class="card" style="padding:0; overflow:hidden;">
                ${data.directions.map(step => {
                    if (step.type === 'warning') return `<div class="step-item warning">⚠️ ${step.text}</div>`;
                    stepCount++;
                    return `<div class="step-item"><div class="step-num">${stepCount}</div><div>${step.text}${step.distance ? ` <span style="color:var(--blue-muted); font-size:0.9em;">(${step.distance})</span>` : ''}</div></div>`;
                }).join('')}
            </div>`;
    }

    resultsDiv.innerHTML = `
        <div class="route-summary">
            <div class="route-stat"><div class="route-stat-num">${data.distance_miles}</div><div class="route-stat-label">Miles</div></div>
            <div class="route-stat"><div class="route-stat-num">${data.duration_hours}</div><div class="route-stat-label">Hours</div></div>
            <div class="route-stat"><div class="route-stat-num">${data.states_on_route.length}</div><div class="route-stat-label">States</div></div>
            <div class="route-stat"><div class="route-stat-num" style="color:${highRiskColor}">${data.high_risk_states}</div><div class="route-stat-label">High Risk</div></div>
        </div>
        <p style="font-size:0.82em; color:var(--blue-muted); margin-bottom:14px;">${data.origin} → ${data.destination} via ${data.route_summary}</p>
        <div class="section-divider">States Along Your Route</div>
        ${statesHtml}
        ${directionsHtml}`;
}

function fetchStateStops(stateName) {
    openInfoDrawer('submit');
}

function getSelectedCategories() {
    const active = document.querySelectorAll('.cat-pill.active');
    return Array.from(active).map(p => p.dataset.cat).join(',');
}

function displaySafeStops(data) {
    const el = document.getElementById('safe-stops-section');
    if (!data.found || !data.waypoints || data.waypoints.length === 0) {
        el.innerHTML = `<div class="card"><p style="color:var(--blue-muted); font-size:0.85em;">No safe stops found along this route. Try adjusting your interval or categories.</p></div>`;
        return;
    }

    el.innerHTML = data.waypoints.map(wp => `
        <div class="safe-stop-card">
            <div class="safe-stop-header-row">
                <div class="teal-pulse"></div>
                <div>
                    <div class="safe-stop-title">Safe stops · ~${wp.hours_in} hrs in</div>
                    <div class="safe-stop-sub">${wp.city}</div>
                </div>
            </div>
            ${wp.stops.length > 0 ? wp.stops.map(s => `
                <div class="stop-row">
                    <div class="stop-cat-icon">${getCatIcon(s.category)}</div>
                    <div class="stop-info">
                        <div class="stop-name">${s.name}</div>
                        <div class="stop-meta">${s.category}${s.tags && s.tags.length > 0 ? ' · ' + s.tags.join(' · ') : ''}${s.source === 'OpenStreetMap' ? ' · via OpenStreetMap' : ''}</div>
                    </div>
                    <div class="stop-right">
                        <div class="stop-score ${getScoreClass(s.score)}">${s.score}</div>
                        <div class="stop-dist">${s.distance_miles} mi</div>
                    </div>
                </div>`).join('') : '<p style="font-size:0.82em; color:var(--blue-muted); padding:8px 0;">No scored businesses found nearby. Try a different interval.</p>'}
            <div class="stop-row submit-stop-row" onclick="openInfoDrawer('submit')">
                <div class="stop-cat-icon teal-plus">+</div>
                <div class="stop-info">
                    <div class="stop-name" style="color:var(--teal);">Know a safe stop near here?</div>
                    <div class="stop-meta">Submit a community recommendation</div>
                </div>
            </div>
        </div>`).join('');
}

function getCatIcon(category) {
    const icons = { 'Food': '🍽', 'Gas': '⛽', 'Coffee': '☕', 'Lodging': '🛏', 'Pharmacy': '💊', 'Rest Stop': '🌿' };
    return icons[category] || '📍';
}

// ===== TIPS =====
const TIPS = ["Before buying from a large retailer, check their ESG score and human rights record. Companies with poor labor practices often score below 50.","When traveling, search your destination state before you go. States with active NAACP or HRC travel advisories may require extra precautions.","Credit unions and community banks typically score higher than major banks like Wells Fargo or Citibank, which have histories of predatory lending.","Fast fashion brands like Shein and Fashion Nova have some of the worst supply chain human rights records. Consider thrift stores or ethical brands.","Police violence data shows accountability rates are often below 5%. When traveling to a new city, check local enforcement records in the Safe Travel Guide.","Small local businesses are rarely in our database — which often means they haven't been flagged for major violations. Supporting local is often the most conscious choice."];
const TRAVEL_TIPS = ["Always check the Safe Travel Guide before visiting a new state. NAACP and HRC advisories are updated regularly.","Even in high-risk states, major cities like Atlanta, Nashville, and Houston often have stronger local protections. Search the city specifically.","If you are transgender and require medical care while traveling, check the state's healthcare laws first. Several states restrict gender-affirming care.","The police violence data shows real incident records. States with accountability rates below 5% have historically offered little recourse for victims.","Religious minority travelers may find rural areas of certain states less accommodating. Urban areas are generally safer.","Disability accessibility varies widely even within states. Always call ahead to verify accessibility at specific venues."];

let currentTip = 0;
let currentTravelTip = 0;

function selectInterval(btn) {
    document.querySelectorAll('.drive-opt').forEach(b => b.classList.remove('selected'));
    btn.classList.add('selected');
    const customWrap = document.getElementById('custom-interval-wrap');
    if (btn.dataset.hours === 'custom') {
        customWrap.style.display = 'block';
    } else {
        customWrap.style.display = 'none';
    }
}

function toggleCat(btn) {
    btn.classList.toggle('active');
}

function showDriveInterval() {
    document.getElementById('drive-interval-section').style.display = 'block';
}

function showTip() { document.getElementById('tips-body').textContent = TIPS[currentTip]; document.getElementById('tips-counter').textContent = `${currentTip + 1} / ${TIPS.length}`; }
function nextTip() { currentTip = (currentTip + 1) % TIPS.length; showTip(); }
function prevTip() { currentTip = (currentTip - 1 + TIPS.length) % TIPS.length; showTip(); }
function showTravelTip() { document.getElementById('travel-tips-body').textContent = TRAVEL_TIPS[currentTravelTip]; document.getElementById('travel-tips-counter').textContent = `${currentTravelTip + 1} / ${TRAVEL_TIPS.length}`; }
function nextTravelTip() { currentTravelTip = (currentTravelTip + 1) % TRAVEL_TIPS.length; showTravelTip(); }
function prevTravelTip() { currentTravelTip = (currentTravelTip - 1 + TRAVEL_TIPS.length) % TRAVEL_TIPS.length; showTravelTip(); }

showTip();
showTravelTip();
updateCompanyCount();
updateSourceCount();

if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
        navigator.serviceWorker.register('/service_worker.js').then(() => console.log('SW registered')).catch(err => console.log('SW error:', err));
    });
}
