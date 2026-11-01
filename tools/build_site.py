import json, html as H, re, os
TOOLS = os.path.dirname(os.path.abspath(__file__))
R = os.path.dirname(TOOLS) + "/"
D = {"en": {}, "ar": {}}
def add(k, en, ar): D["en"][k] = en; D["ar"][k] = ar; return k
def i(k): return f'data-i18n="{k}"'
def en(k): return H.escape(D["en"][k], quote=False)
def S(tag, k, cls="", extra=""):
    c = f' class="{cls}"' if cls else ""
    return f'<{tag}{c} {i(k)}{extra}>{en(k)}</{tag}>'
def ic(n, cls="icon"): return f'<svg class="{cls}"><use href="#i-{n}"/></svg>'
WAI = ic("wa", "")

# ---------- shared strings ----------
for k, e, a in [
 ("nav.home","Home","الرئيسية"),("nav.services","Services","الخدمات"),("nav.atlas","ATLAS™","أطلس™"),("nav.portfolio","Portfolio","الأعمال"),("nav.about","About","من نحن"),("nav.contact","Contact","تواصل"),
 ("lang.btn","العربية","English"),
 ("hero.eyebrow","AashiFX™ · Brand-to-Business Integrator","AashiFX™ · من العلامة إلى الأعمال"),
 ("hero.title","Creative Studio with Soul","استوديو إبداعي بروح"),
 ("hero.sub","Branding, documents, IT, trade, mobility and equipment under one roof. Across India and the GCC.","العلامة والمستندات والتقنية والتجارة والتنقل والمعدات تحت مظلة واحدة. في الهند ودول الخليج."),
 ("hero.tag","Design. Document. Deliver.","صمّم. وثّق. سلّم."),
 ("hero.cta","Chat on WhatsApp","تحدّث عبر واتساب"),("hero.cta2","See the six pillars","تعرّف على الركائز الست"),
 ("pill.eyebrow","Six pillars","ست ركائز"),("pill.title","One establishment. One identity.","مؤسسة واحدة. هوية واحدة."),
 ("pill.sub","BrandX | OfficeX | TechX | TradeX | DriveX | PowerX","BrandX | OfficeX | TechX | TradeX | DriveX | PowerX"),
 ("atlas.eyebrow","Executive Intelligence","الذكاء التنفيذي"),("atlas.sys","An AashiFX Intelligence System","نظام ذكاء من AashiFX"),("atlas.title","ATLAS™","أطلس™"),
 ("atlas.sub","Clear, curated news in three languages. Short reads, no noise.","أخبار مختارة وواضحة بثلاث لغات. قراءة قصيرة بلا ضجيج."),
 ("atlas.cta","Open ATLAS™","افتح أطلس™"),
 ("work.eyebrow","Selected work","أعمال مختارة"),("work.title","Portfolio","الأعمال"),
 ("work.sub","Anonymised samples. Client names stay private.","نماذج بدون أسماء. أسماء العملاء تبقى سرّية."),
 ("w1.t","Brand identity kit","حزمة هوية بصرية"),("w1.d","Fintech startup · Client under NDA","شركة تقنية مالية ناشئة · عميل بموجب اتفاقية سرية"),
 ("w2.t","Company profile · Car rental","ملف تعريفي · تأجير سيارات"),("w2.d","Rental company · Client under NDA","شركة تأجير · عميل بموجب اتفاقية سرية"),
 ("w3.t","Company profile · Heavy equipment","ملف تعريفي · معدات ثقيلة"),("w3.d","Equipment rental · Client under NDA","تأجير معدات · عميل بموجب اتفاقية سرية"),
 ("work.cta","View portfolio","عرض الأعمال"),
 ("about.eyebrow","The founder","المؤسس"),("about.role","Founder & Creative Director","المؤسس والمدير الإبداعي"),
 ("about.p","Design with discipline, delivered with soul. One person accountable for every detail.","تصميم بانضباط، وتنفيذ بروح. شخص واحد مسؤول عن كل التفاصيل."),
 ("about.l1","Clear ownership, no hand-offs","مسؤولية واضحة بدون وسطاء"),("about.l2","Simple process, fast turnaround","إجراءات بسيطة وتسليم سريع"),("about.l3","Quality over noise","الجودة قبل الضجيج"),
 ("about.cta","More about us","المزيد عنا"),
 ("final.title","Let's build something with soul","لنصنع شيئاً بروح"),("final.sub","Tell us what you need. We reply on WhatsApp.","أخبرنا بما تحتاجه. نردّ عبر واتساب."),("final.cta2","Contact page","صفحة التواصل"),
 ("foot.line","Six Pillars. One Establishment. One Identity.","ست ركائز. مؤسسة واحدة. هوية واحدة."),
 ("foot.reach","Operating across India and the GCC region.","نعمل في الهند ودول الخليج."),
 ("foot.rights","© 2026 AashiFX™. All rights reserved.","© 2026 AashiFX™. جميع الحقوق محفوظة."),
]: add(k, e, a)

# ---------- pillars ----------
PILLARS = [
 ("brand","BrandX","brand","Branding & Creative Design","الهوية والتصميم الإبداعي","Logos to campaigns. Brands that look and feel right.","من الشعارات إلى الحملات. علامات تبدو وتُشعر بالصواب.",
  ["Logo design and brand identity","Corporate branding","Graphic design","Flyers, posters and banners","Social media creatives","Brochures, catalogues and company profiles","Marketing and advertising materials","Creative strategy and visual communication"],
  ["تصميم الشعارات والهوية البصرية","الهوية المؤسسية","التصميم الجرافيكي","فلايرات وبوسترات ولافتات","تصاميم وسائل التواصل الاجتماعي","بروشورات وكتالوجات وملفات تعريفية","مواد تسويقية وإعلانية","الاستراتيجية الإبداعية والتواصل البصري"]),
 ("office","OfficeX","docs","SmartDocs & Business Documentation","المستندات الذكية والتوثيق المكتبي","Documents that run your office, in English and Arabic.","مستندات تُدير مكتبك، بالإنجليزية والعربية.",
  ["Quotations and invoices","Business proposals","Company profiles","Reports and statements","SOPs and business templates","Agreements and business letters","Bilingual documentation (English/Arabic)","Office administration and documentation systems"],
  ["عروض الأسعار والفواتير","مقترحات الأعمال","الملفات التعريفية للشركات","التقارير والكشوف","إجراءات التشغيل القياسية وقوالب الأعمال","الاتفاقيات والخطابات التجارية","توثيق ثنائي اللغة (إنجليزي/عربي)","الإدارة المكتبية وأنظمة التوثيق"]),
 ("tech","TechX","it","IT & Digital Solutions","الحلول التقنية والرقمية","IT support and digital systems that just work.","دعم تقني وأنظمة رقمية تعمل بكفاءة.",
  ["Computer and laptop support","Operating system installation","Software installation and deployment","Networking and infrastructure","Windows Server and system administration","Data backup and recovery","Troubleshooting and maintenance","System integration and automation"],
  ["دعم الحواسيب واللابتوبات","تثبيت أنظمة التشغيل","تثبيت البرمجيات ونشرها","الشبكات والبنية التحتية","إدارة Windows Server والأنظمة","النسخ الاحتياطي واستعادة البيانات","استكشاف الأعطال والصيانة","تكامل الأنظمة والأتمتة"]),
 ("trade","TradeX","trade","Trading, Procurement & Supply","التجارة والمشتريات والتوريد","Sourcing, procurement and supply across categories.","توريد ومشتريات وتجارة متعددة الفئات.",
  ["General trading","Industrial and commercial supplies","Product sourcing","Procurement and purchasing support","Vendor coordination","Safety materials and equipment","Medical and scientific equipment","Laboratory equipment","Multi-category product supply"],
  ["التجارة العامة","التوريدات الصناعية والتجارية","البحث عن المنتجات وتوريدها","دعم المشتريات والتوريد","التنسيق مع الموردين","مواد ومعدات السلامة","المعدات الطبية والعلمية","معدات المختبرات","توريد منتجات متعددة الفئات"]),
 ("drive","DriveX","drive","Transportation & Mobility","النقل والتنقل","Cars, fleets and logistics for people and companies.","سيارات وأساطيل وخدمات لوجستية للأفراد والشركات.",
  ["Car rental services","Corporate vehicle rental","Transportation solutions","Fleet management support","Vehicle operations","Mobility solutions","Logistics coordination"],
  ["خدمات تأجير السيارات","تأجير المركبات للشركات","حلول النقل","دعم إدارة الأساطيل","تشغيل المركبات","حلول التنقل","تنسيق الخدمات اللوجستية"]),
 ("power","PowerX","power","Equipment & Industrial Support","المعدات والدعم الصناعي","Equipment, machinery and site support.","معدات وآليات ودعم للمواقع.",
  ["Equipment rental","Heavy machinery support","Generator rental and supply","Industrial equipment","Scientific equipment","Site operational support","Equipment sourcing","Manpower and operational assistance"],
  ["تأجير المعدات","دعم الآليات الثقيلة","تأجير وتوريد المولدات","المعدات الصناعية","المعدات العلمية","دعم العمليات في المواقع","توريد المعدات","الدعم التشغيلي والعمالة"]),
]
for k,name,icon,ne,na,de,da,pe,pa in PILLARS:
    add(f"s.{k}.t",name,name); add(f"s.{k}.n",ne,na); add(f"s.{k}.d",de,da)
    for n,(x,y) in enumerate(zip(pe,pa),1): add(f"sv.{k}.p{n}",x,y)
add("sv.eyebrow","What we do","ماذا نقدّم"); add("sv.title","Services","الخدمات")
add("sv.sub","Six pillars. One establishment. Each pillar can grow without adding new divisions.","ست ركائز. مؤسسة واحدة. تتوسّع كل ركيزة دون إضافة أقسام جديدة.")
add("sv.ask","Ask on WhatsApp","اسأل عبر واتساب")

# ---------- deep content ----------
SLUG = {"brand":"brandx","office":"officex","tech":"techx","trade":"tradex","drive":"drivex","power":"powerx"}
for k,e,a in [
 ("pill.more","Explore","استكشف"),
 ("why.eyebrow","Why AashiFX™","لماذا AashiFX™"),("why.title","One establishment. Everything connected.","مؤسسة واحدة. كل شيء متصل."),
 ("why.1","One identity","هوية واحدة"),("why.1d","Your brand, documents, systems and operations stay consistent.","علامتك ومستنداتك وأنظمتك وعملياتك تبقى متسقة."),
 ("why.2","Six pillars, one contact","ست ركائز، جهة اتصال واحدة"),("why.2d","One team and one WhatsApp chat for every need.","فريق واحد ومحادثة واتساب واحدة لكل احتياج."),
 ("why.3","Bilingual by default","ثنائي اللغة افتراضياً"),("why.3d","English and Arabic documents, designs and support.","مستندات وتصاميم ودعم بالإنجليزية والعربية."),
 ("why.4","India and the GCC","الهند ودول الخليج"),("why.4d","Operating across both regions.","نعمل في المنطقتين."),
 ("jr.eyebrow","The connected model","النموذج المتكامل"),("jr.title","One client journey","رحلة عميل واحدة"),
 ("jr.sub","See how the pillars connect when a business starts, grows and operates.","شاهد كيف تترابط الركائز عندما تبدأ الشركة وتنمو وتعمل."),
 ("jr.brand","Create the identity.","ابنِ الهوية."),("jr.office","Document the business.","وثّق الأعمال."),("jr.tech","Set up the systems.","جهّز الأنظمة."),
 ("jr.trade","Source what you need.","وفّر ما تحتاجه."),("jr.drive","Move people and goods.","حرّك الأفراد والبضائع."),("jr.power","Equip the operation.","جهّز العمليات."),
 ("faq.title","Common questions","أسئلة شائعة"),
 ("hq1","What is AashiFX™?","ما هي AashiFX™؟"),("ha1","A creative and business solutions establishment with six pillars, working across India and the GCC.","مؤسسة حلول إبداعية وتجارية بست ركائز، تعمل في الهند ودول الخليج."),
 ("hq2","Do I need to use all six pillars?","هل أحتاج إلى استخدام الركائز الست؟"),("ha2","No. Start with one and add others when you need them.","لا. ابدأ بواحدة وأضف غيرها عند الحاجة."),
 ("hq3","How do I get started?","كيف أبدأ؟"),("ha3","Send a WhatsApp message with what you need. We reply there first.","أرسل رسالة واتساب بما تحتاجه. نردّ عليك هناك أولاً."),
 ("hq4","Do you work in Arabic?","هل تعملون بالعربية؟"),("ha4","Yes. Documents, designs and support are available in English and Arabic.","نعم. المستندات والتصاميم والدعم متاحة بالإنجليزية والعربية."),
 ("pg.what","What we do","ماذا نقدّم"),("pg.ideal","Ideal for","مناسب لـ"),("pg.deliv","Typical deliverables","مخرجات نموذجية"),
 ("pg.proc","How it works","كيف نعمل"),("pg.pairs","Works well with","يعمل جيداً مع"),("pg.back","All services","كل الخدمات"),
 ("pg.s1","Brief","الطلب"),("pg.s2","Build","التنفيذ"),("pg.s3","Deliver","التسليم"),
 ("pg.cta","Start with a WhatsApp message","ابدأ برسالة واتساب"),("pg.ctasub","Tell us what you need. We reply there first.","أخبرنا بما تحتاجه. نردّ عليك هناك أولاً."),
 ("sv.more","View details","عرض التفاصيل"),
]: add(k,e,a)

PG = {
"brand": dict(
 intro=("Brands that look consistent and feel intentional, from the first logo to the last brochure.","علامات متسقة في مظهرها ومقصودة في إحساسها، من أول شعار إلى آخر بروشور."),
 ideal=[("New businesses that need a first identity","شركات جديدة تحتاج هوية أولى"),("Established companies refreshing their look","شركات قائمة تجدّد مظهرها"),("Teams that need steady social and print material","فرق تحتاج مواد اجتماعية ومطبوعة باستمرار")],
 deliv=[("Logo files for print and screen","ملفات الشعار للطباعة والشاشة"),("Colour and typography guide","دليل الألوان والخطوط"),("Social media templates","قوالب وسائل التواصل"),("Print-ready artwork","ملفات جاهزة للطباعة")],
 steps=[("Share your business, audience and style references.","شاركنا نشاطك وجمهورك ومراجعك الجمالية."),("We design concepts, then refine the one you choose.","نصمّم أفكاراً ثم نطوّر ما تختاره."),("You receive final files, ready for print and digital.","تستلم الملفات النهائية جاهزة للطباعة والاستخدام الرقمي.")],
 faq=[("Can you work from an existing logo?","هل يمكنكم العمل على شعار موجود؟","Yes. We can refresh it, extend it into a full brand kit, or build material around it as it is.","نعم. يمكننا تجديده أو توسيعه إلى حزمة هوية كاملة أو بناء المواد حوله كما هو."),
      ("Can designs be bilingual?","هل يمكن أن تكون التصاميم ثنائية اللغة؟","Yes. Layouts and social material can be in English, Arabic or both.","نعم. يمكن أن تكون التصاميم بالإنجليزية أو العربية أو بكلتيهما.")],
 pairs=["office","tech"]),
"office": dict(
 intro=("Business documents that look professional, read clearly and can be reused, in English and Arabic.","مستندات أعمال احترافية المظهر وواضحة ويمكن إعادة استخدامها، بالإنجليزية والعربية."),
 ideal=[("Companies sending quotations and invoices regularly","شركات ترسل عروض أسعار وفواتير بانتظام"),("Offices that need standard procedures and templates","مكاتب تحتاج إجراءات وقوالب موحّدة"),("Businesses working with Arabic and English clients","شركات تتعامل مع عملاء بالعربية والإنجليزية")],
 deliv=[("Branded quotation and invoice templates","قوالب عروض أسعار وفواتير بهوية الشركة"),("Proposals and company profiles","مقترحات وملفات تعريفية"),("SOP documents and business letters","وثائق إجراءات وخطابات تجارية"),("Bilingual document sets","مجموعات مستندات ثنائية اللغة")],
 steps=[("Tell us which documents your business uses most.","أخبرنا بالمستندات التي تستخدمها شركتك أكثر."),("We structure, write and format them with your branding.","نرتّبها ونصيغها وننسّقها بهويتك."),("You get editable files and a simple system to reuse them.","تستلم ملفات قابلة للتعديل ونظاماً بسيطاً لإعادة استخدامها.")],
 faq=[("Can documents be bilingual?","هل يمكن أن تكون المستندات ثنائية اللغة؟","Yes. English and Arabic side by side, or as separate versions.","نعم. بالإنجليزية والعربية جنباً إلى جنب أو كنسخ منفصلة."),
      ("Can you build templates we reuse ourselves?","هل يمكنكم إعداد قوالب نعيد استخدامها بأنفسنا؟","Yes. We build templates with your branding so your team can reuse them.","نعم. نبني القوالب بهويتك ليعيد فريقك استخدامها.")],
 pairs=["brand","trade"]),
"tech": dict(
 intro=("IT support and digital systems that keep your office running and your tools connected.","دعم تقني وأنظمة رقمية تُبقي مكتبك يعمل وأدواتك متصلة."),
 ideal=[("Offices that need reliable day-to-day IT support","مكاتب تحتاج دعماً تقنياً يومياً موثوقاً"),("Teams setting up new computers, networks or servers","فرق تجهّز حواسيب أو شبكات أو خوادم جديدة"),("Businesses that want repetitive tasks automated","شركات تريد أتمتة المهام المتكررة")],
 deliv=[("Configured computers and software","حواسيب وبرمجيات مهيأة"),("Network and server setup","تجهيز الشبكات والخوادم"),("Backup and recovery plan","خطة نسخ احتياطي واستعادة"),("Documented systems and automations","أنظمة وأتمتة موثّقة")],
 steps=[("Describe the problem or the setup you need.","اشرح المشكلة أو التجهيز الذي تحتاجه."),("We diagnose, install, configure or integrate.","نشخّص ونثبّت ونهيّئ أو نربط الأنظمة."),("We hand over a working setup with notes and support.","نسلّم نظاماً يعمل مع ملاحظات ودعم.")],
 faq=[("Do you support offices as well as single computers?","هل تدعمون المكاتب والأجهزة الفردية؟","Yes. From a single laptop to office networks and servers.","نعم. من لابتوب واحد إلى شبكات المكاتب والخوادم."),
      ("Can you automate repetitive tasks?","هل يمكنكم أتمتة المهام المتكررة؟","Yes. We connect your tools and automate routine steps where it makes sense.","نعم. نربط أدواتك ونؤتمت الخطوات الروتينية عند الجدوى.")],
 pairs=["office","power"]),
"trade": dict(
 intro=("Sourcing, procurement and supply across industrial, safety, medical and laboratory categories.","توريد ومشتريات وتجارة في المجالات الصناعية والسلامة والطبية والمخبرية."),
 ideal=[("Companies that need a single supplier for many categories","شركات تحتاج مورّداً واحداً لفئات متعددة"),("Teams buying safety, medical or lab equipment","فرق تشتري معدات سلامة أو طبية أو مخبرية"),("Businesses that want help with vendor coordination","شركات تريد مساعدة في التنسيق مع الموردين")],
 deliv=[("Sourced product options","خيارات منتجات مصدّرة"),("Vendor coordination and follow-up","تنسيق ومتابعة مع الموردين"),("Purchase documentation","مستندات الشراء"),("Delivered supply","توريد مسلّم")],
 steps=[("Send the item list or specification.","أرسل قائمة الأصناف أو المواصفات."),("We source, compare and coordinate with vendors.","نبحث ونقارن وننسّق مع الموردين."),("Items are supplied with the documents you need.","تُورَّد الأصناف مع المستندات التي تحتاجها.")],
 faq=[("Can you source products that are not on your list?","هل يمكنكم توفير منتجات غير مذكورة؟","Send the specification. We check availability and coordinate with vendors.","أرسل المواصفات. نتحقق من التوفر وننسّق مع الموردين."),
      ("Who do you supply?","لمن تقدّمون التوريد؟","Mostly businesses and organisations. Send your requirement and we confirm what we can do.","غالباً الشركات والمؤسسات. أرسل طلبك ونؤكد ما يمكننا تنفيذه.")],
 pairs=["drive","office"]),
"drive": dict(
 intro=("Vehicles and mobility for individuals and companies, with fleet and logistics support.","مركبات وحلول تنقل للأفراد والشركات، مع دعم الأساطيل والخدمات اللوجستية."),
 ideal=[("Individuals needing a rental car","أفراد يحتاجون سيارة للإيجار"),("Companies needing corporate vehicle rental","شركات تحتاج تأجير مركبات للشركات"),("Teams managing vehicles and routes","فرق تدير المركبات والمسارات")],
 deliv=[("Rental vehicles for your period","مركبات للإيجار لمدتك"),("Corporate rental arrangements","ترتيبات تأجير للشركات"),("Fleet management support","دعم إدارة الأسطول"),("Coordinated logistics","خدمات لوجستية منسّقة")],
 steps=[("Tell us the vehicle type, period and location.","أخبرنا بنوع المركبة والمدة والموقع."),("We arrange the vehicle or transport plan.","نرتّب المركبة أو خطة النقل."),("You get the vehicle or service, with follow-up support.","تستلم المركبة أو الخدمة مع دعم المتابعة.")],
 faq=[("Do you offer corporate rental?","هل تقدمون تأجيراً للشركات؟","Yes. Corporate vehicle rental and fleet support are part of DriveX.","نعم. تأجير مركبات الشركات ودعم الأسطول جزء من DriveX."),
      ("Can you help with logistics coordination?","هل يمكنكم المساعدة في تنسيق الخدمات اللوجستية؟","Yes. Share the route and schedule and we coordinate the movement.","نعم. شاركنا المسار والجدول وننسّق النقل.")],
 pairs=["power","tech"]),
"power": dict(
 intro=("Equipment, machinery and on-site support for industrial and operational needs.","معدات وآليات ودعم ميداني للاحتياجات الصناعية والتشغيلية."),
 ideal=[("Sites needing equipment or generators on hire","مواقع تحتاج معدات أو مولدات للإيجار"),("Projects needing heavy machinery support","مشاريع تحتاج دعم آليات ثقيلة"),("Operations needing extra manpower and assistance","عمليات تحتاج عمالة ودعماً إضافياً")],
 deliv=[("Equipment on rental or supply","معدات للإيجار أو التوريد"),("Generator rental and supply","تأجير وتوريد المولدات"),("Site operational support","دعم تشغيلي في الموقع"),("Sourced equipment","معدات يتم توريدها")],
 steps=[("Describe the site, equipment and duration.","اشرح الموقع والمعدات والمدة."),("We arrange equipment, machinery and support.","نرتّب المعدات والآليات والدعم."),("Equipment and support arrive ready for the site.","تصل المعدات والدعم جاهزة للموقع.")],
 faq=[("Do you rent generators and equipment?","هل تؤجرون المولدات والمعدات؟","Yes. Equipment and generator rental and supply are part of PowerX.","نعم. تأجير وتوريد المعدات والمولدات جزء من PowerX."),
      ("Can you support us on site?","هل يمكنكم دعمنا في الموقع؟","Yes. We offer site operational support, including manpower and operational assistance.","نعم. نقدّم دعماً تشغيلياً في الموقع، يشمل العمالة والمساعدة التشغيلية.")],
 pairs=["drive","trade"]),
}
for k,d in PG.items():
    add(f"pg.{k}.intro",*d["intro"])
    for n,(x,y) in enumerate(d["ideal"],1): add(f"pg.{k}.i{n}",x,y)
    for n,(x,y) in enumerate(d["deliv"],1): add(f"pg.{k}.d{n}",x,y)
    for n,(x,y) in enumerate(d["steps"],1): add(f"pg.{k}.s{n}",x,y)
    for n,(qe,qa,ae,aa) in enumerate(d["faq"],1): add(f"pg.{k}.q{n}",qe,qa); add(f"pg.{k}.a{n}",ae,aa)
PILL = {p[0]:p for p in PILLARS}
FOOTNAV = '<nav class="foot-nav" aria-label="Pillars">' + ''.join(f'<a href="{SLUG[p[0]]}.html">{p[1]}</a>' for p in PILLARS) + '</nav>'

# ---------- sub-services + illustrations ----------
ill = {}; exec(open(os.path.join(TOOLS, "illustrations.py")).read(), ill)
_sn = {}; exec(open(os.path.join(TOOLS, "subservices.py")).read(), _sn); SUBS = _sn["SUBS"]
os.makedirs(R + "assets/art", exist_ok=True)
for k_, e_, a_ in [("sub.get","What you get","ما تحصل عليه"),("sub.more","More from this pillar","المزيد من هذه الركيزة")]: add(k_, e_, a_)
SUBLIST = {}
for k_, items_ in SUBS.items():
    SUBLIST[k_] = []
    for n_, (slug_, de_, da_, ge_, ga_) in enumerate(items_, 1):
        sid_ = SLUG[k_] + "-" + slug_
        add(f"sub.{sid_}.d", de_, da_)
        for m_, (x_, y_) in enumerate(zip(ge_, ga_), 1): add(f"sub.{sid_}.g{m_}", x_, y_)
        SUBLIST[k_].append((sid_, f"sv.{k_}.p{n_}", slug_))
        assert slug_ in ill["S_"], slug_
        open(R + f"assets/art/{sid_}.svg", "w").write(ill["render"](slug_, k_, n_ + len(SLUG)))
for name_, pil_ in [("page-contact","site"),("page-about","site"),("page-portfolio","site"),("page-services","site"),("profile-car","drive"),("profile-heavy","power")]:
    open(R + f"assets/art/{name_}.svg", "w").write(ill["render"](name_, pil_, 3))
def chip_link(k, n):
    sid, tk, _ = SUBLIST[k][n-1]
    return f'<li class="chip"><a href="{sid}.html" {i(tk)}>{en(tk)}</a></li>'
def img_art(name, eager=False):
    a = 'fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
    return f'<img src="assets/art/{name}.svg" width="800" height="600" alt="" {a}>'
def pbanner(art, eb, t, s_, h1=None):
    h = h1 or S("h1", t)
    return f'<div class="banner short">{img_art(art, True)}<div class="over"><div class="wrap">{S("p",eb,"eyebrow")}{h}{S("p",s_,"lead")}</div></div></div>'

# ---------- chrome ----------
SPRITE = '''<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>
<symbol id="i-brand" viewBox="0 0 24 24"><path d="M12 3l9 5-9 5-9-5 9-5zM3 13l9 5 9-5"/></symbol>
<symbol id="i-docs" viewBox="0 0 24 24"><path d="M7 3h7l5 5v13H7zM14 3v5h5M10 13h6M10 17h6"/></symbol>
<symbol id="i-it" viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="16" rx="2"/><path d="M7 9l3 3-3 3M13 15h4"/></symbol>
<symbol id="i-trade" viewBox="0 0 24 24"><path d="M3 8l9-5 9 5v8l-9 5-9-5zM3 8l9 5 9-5M12 13v8"/></symbol>
<symbol id="i-drive" viewBox="0 0 24 24"><path d="M4 16l1.6-5.2A2 2 0 0 1 7.500 9.500h9a2 2 0 0 1 1.900 1.300L20 16M3 16h18v3H3zM7 19v1.500M17 19v1.500"/></symbol>
<symbol id="i-power" viewBox="0 0 24 24"><path d="M13 2L4 14h7l-1 8 9-12h-7z"/></symbol>
<symbol id="i-globe" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18"/></symbol>
<symbol id="i-wa" viewBox="0 0 24 24"><path d="M3 21l1.6-4.7A8.5 8.5 0 1 1 8 19.6zM9 9c0 3 3 6 6 6l1-2-2-1-1 .8c-.8-.4-1.6-1.2-2-2l.8-1-1-2z"/></symbol>
</defs></svg>'''
def nav(cur):
    links = [("index","nav.home"),("services","nav.services"),("atlas","nav.atlas"),("portfolio","nav.portfolio"),("about","nav.about"),("contact","nav.contact")]
    a = ''.join(f'<a href="{p}.html"{" aria-current=\"page\"" if p==cur else ""} {i(k)}>{en(k)}</a>' for p,k in links)
    return f'''<header class="nav"><div class="wrap">
  <a class="logo" href="index.html" aria-label="AashiFX™ home">Aashi<b>FX</b><sup>™</sup></a>
  <nav class="menu" id="menu" aria-label="Main">{a}</nav>
  <div class="tools">
    <button class="theme" data-theme-toggle type="button" aria-label="Light / Dark"><svg class="moon" viewBox="0 0 24 24"><path d="M20 14.5A8 8 0 1 1 9.500 4a6.500 6.500 0 0 0 10.500 10.500z"/></svg><svg class="sun" viewBox="0 0 24 24"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M2 12h2M20 12h2M4.900 4.900l1.400 1.400M17.700 17.700l1.400 1.400M4.900 19.100l1.400-1.400M17.700 6.300l1.400-1.400"/></svg></button>
    <button class="lang" data-lang-toggle type="button" {i("lang.btn")}>{en("lang.btn")}</button>
    <button class="burger" data-burger type="button" aria-expanded="false" aria-controls="menu" aria-label="Menu">☰</button>
  </div>
</div></header>'''
FOOT = f'''<footer><div class="wrap">{FOOTNAV}
  <p class="foot-line" {i("foot.line")}>{en("foot.line")}</p>
  <p {i("foot.reach")}>{en("foot.reach")}</p>
  <p {i("foot.rights")}>{en("foot.rights")}</p>
</div></footer>
<a class="wa-fab" data-wa href="https://wa.me/" rel="noopener" aria-label="WhatsApp">{WAI}</a>'''
def page(cur, title, desc, main):
    return f'''<!doctype html>
<html lang="en" dir="ltr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#04060e">
<meta name="color-scheme" content="dark light">
<script>try{{var t=localStorage.getItem("theme");if(t)document.documentElement.setAttribute("data-theme",t)}}catch(e){{}}</script>
<link rel="icon" type="image/png" href="assets/favicon.png">
<link rel="apple-touch-icon" href="assets/apple-touch-icon.png">
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
{SPRITE}
{nav(cur)}
<main>
{main}
</main>
{FOOT}
<script src="assets/app.js" defer></script>
</body>
</html>
'''
def wa_btn(topic, key, cls="btn btn-ghost"):
    t = f' data-wa-topic="{topic}"' if topic else ""
    return f'<a class="{cls}" data-wa{t} href="https://wa.me/" rel="noopener">{WAI}<span {i(key)}>{en(key)}</span></a>'
def phero(eb, t, s, h1=None):
    h = h1 or S("h1", t)
    return f'<section class="page-hero"><div class="wrap">{S("p",eb,"eyebrow")}{h}{S("p",s,"lead")}</div></section>'
def pts(prefix, n): return '<ul class="points">'+''.join(f'<li {i(f"{prefix}.p{x}")}>{en(f"{prefix}.p{x}")}</li>' for x in range(1,n+1))+'</ul>'
TOPICS = {"brand":"BrandX","office":"OfficeX","tech":"TechX","trade":"TradeX","drive":"DriveX","power":"PowerX"}

# ---------- Home (picture-first) ----------
for k_,e_,a_ in [("f1","6 pillars","6 ركائز"),("f2","English · Arabic","إنجليزي · عربي"),("f3","India · GCC","الهند · الخليج")]: add(k_,e_,a_)
def art_img(k, alt=""): return f'<img src="assets/art/{SLUG[k]}.svg" width="800" height="600" alt="{alt}" loading="lazy" decoding="async">'
def faq_item(qk, ak): return f'<details class="faq"><summary {i(qk)}>{en(qk)}</summary><p {i(ak)}>{en(ak)}</p></details>'
def tile_link(k, big=False):
    return f'<a class="art r43" href="{SLUG[k]}.html">{art_img(k)}<span class="cap"><b>{PILL[k][1]}</b><small {i(f"s.{k}.n")}>{en(f"s.{k}.n")}</small></span></a>'
mosaic = ''.join(tile_link(p[0]) for p in PILLARS)
facts = f'<div class="facts"><span><b {i("f1")}>{en("f1")}</b></span><span {i("f2")}>{en("f2")}</span><span {i("f3")}>{en("f3")}</span><span {i("hero.tag")}>{en("hero.tag")}</span></div>'
def row(k):
    chips = ''.join(chip_link(k,n) for n in (1,2,3))
    return f'<article class="row"><a class="art r169" href="{SLUG[k]}.html" tabindex="-1" aria-hidden="true">{art_img(k)}</a><div><h3>{PILL[k][1]}</h3>{S("p",f"s.{k}.n","n")}{S("p",f"s.{k}.d","d")}<ul class="chipset">{chips}</ul><a class="more" href="{SLUG[k]}.html" {i("pill.more")}>{en("pill.more")}</a></div></article>'
journey = ''.join(f'<li class="card">{ic(PILL[k][2])}<span class="jn">{PILL[k][1]}</span>{S("p",f"jr.{k}")}</li>' for k in SLUG)
def work_tile(n, k): return f'<a class="art r43" href="portfolio.html">{img_art(k)}<span class="cap"><b {i(f"w{n}.t")}>{en(f"w{n}.t")}</b><small {i(f"w{n}.d")}>{en(f"w{n}.d")}</small></span></a>'
home = f'''<section class="hero"><div class="wrap">
  <div>{S("p","hero.eyebrow","eyebrow")}{S("h1","hero.title")}{S("p","hero.sub","lead")}{S("p","hero.tag","tagline")}
  <div class="cta-row">{wa_btn("", "hero.cta", "btn btn-primary")}<a class="btn btn-ghost" href="#pillars" {i("hero.cta2")}>{en("hero.cta2")}</a></div></div>
  <div class="mosaic">{mosaic}</div>
</div></section>
<div class="wrap">{facts}</div>
<section id="pillars"><div class="wrap">
  <div class="sec-head">{S("p","pill.eyebrow","eyebrow")}{S("h2","pill.title")}</div>
  <div class="showcase">{''.join(row(p[0]) for p in PILLARS)}</div>
</div></section>
<section><div class="wrap">
  <div class="sec-head">{S("p","jr.eyebrow","eyebrow")}{S("h2","jr.title")}</div>
  <ol class="journey">{journey}</ol>
</div></section>
<section id="atlas"><div class="wrap"><div class="atlas-box">
  <div>{S("p","atlas.eyebrow","eyebrow")}{S("h2","atlas.title")}{S("p","atlas.sys","sys")}{S("p","atlas.sub","muted")}
  <div class="chips"><span>EN</span><span>AR</span><span>TA</span></div>
  <a class="btn btn-ghost" href="atlas.html" {i("atlas.cta")}>{en("atlas.cta")}</a></div>
  <img class="atlas-art" src="assets/atlas-badge.webp" width="240" height="240" alt="ATLAS™ badge" loading="lazy">
</div></div></section>
<section id="portfolio"><div class="wrap">
  <div class="sec-head">{S("p","work.eyebrow","eyebrow")}{S("h2","work.title")}</div>
  <div class="grid work">{work_tile(1,"brandx-logo-identity")}{work_tile(2,"profile-car")}{work_tile(3,"profile-heavy")}</div>
  <p style="margin-top:1.5rem;text-align:center"><a class="btn btn-ghost" href="portfolio.html" {i("work.cta")}>{en("work.cta")}</a></p>
</div></section>
<section id="about"><div class="wrap about">
  <div class="avatar" aria-hidden="true"><bdi>C™</bdi></div>
  <div>{S("p","about.eyebrow","eyebrow")}<h2><bdi>CHIEF™</bdi></h2>{S("p","about.role","role")}{S("p","about.p","muted")}
  <p style="margin-top:1.25rem"><a class="btn btn-ghost" href="about.html" {i("about.cta")}>{en("about.cta")}</a></p></div>
</div></section>
<section class="final"><div class="wrap">{S("h2","final.title")}
  <div class="cta-row">{wa_btn("", "hero.cta", "btn btn-primary")}<a class="btn btn-ghost" href="contact.html" {i("final.cta2")}>{en("final.cta2")}</a></div>
</div></section>'''
index = page("index","AashiFX™ | Creative Studio with Soul","AashiFX™: Brand-to-Business Integrator. BrandX, OfficeX, TechX, TradeX, DriveX and PowerX across India and the GCC.",home)

# ---------- Services overview ----------
def svc(k,name,icon,*_):
    chips = ''.join(chip_link(k,n) for n in (1,2,3))
    more = f'<a class="btn btn-ghost" href="{SLUG[k]}.html" {i("sv.more")}>{en("sv.more")}</a>'
    return f'<article class="svc-card" id="{k}"><a class="art r169" href="{SLUG[k]}.html">{art_img(k)}<span class="cap"><b>{name}</b><small {i(f"s.{k}.n")}>{en(f"s.{k}.n")}</small></span></a><div class="info"><ul class="chipset">{chips}</ul><div class="cta-row" style="margin-top:.9rem">{more}{wa_btn(TOPICS[k],"sv.ask")}</div></div></article>'
services = page("services","AashiFX™ | Services","Six pillars: BrandX, OfficeX, TechX, TradeX, DriveX and PowerX.",
  pbanner("page-services","sv.eyebrow","sv.title","sv.sub")+f'<section><div class="wrap"><div class="svc-grid">{"".join(svc(*p[:3]) for p in PILLARS)}</div></div></section>')

# ---------- Pillar pages ----------
PILLAR_PAGES = {}
for k,name,icon,*_ in PILLARS:
    nitems = len([x for x in D["en"] if x.startswith(f"sv.{k}.p")])
    allchips = ''.join(chip_link(k,n) for n in range(1,nitems+1))
    ideal = ''.join(f'<li {i(f"pg.{k}.i{n}")}>{en(f"pg.{k}.i{n}")}</li>' for n in (1,2,3))
    deliv = ''.join(f'<li {i(f"pg.{k}.d{n}")}>{en(f"pg.{k}.d{n}")}</li>' for n in (1,2,3,4))
    steps = ''.join(f'<div class="card"><p class="stepn" aria-hidden="true">{n}</p>{S("h3",f"pg.s{n}")}{S("p",f"pg.{k}.s{n}")}</div>' for n in (1,2,3))
    pairs = ''.join(tile_link(q) for q in PG[k]["pairs"])
    faqs = ''.join(faq_item(f"pg.{k}.q{n}",f"pg.{k}.a{n}") for n in (1,2))
    subtiles = ''.join(f'<a class="art r43" href="{sid}.html">{img_art(sid)}<span class="cap"><b {i(tk)}>{en(tk)}</b></span></a>' for sid,tk,_ in SUBLIST[k])
    banner = f'''<div class="banner">{art_img(k).replace('loading="lazy"','fetchpriority="high"')}<div class="over"><div class="wrap"><a class="backlink" href="services.html" {i("pg.back")}>{en("pg.back")}</a>{S("p",f"s.{k}.n","eyebrow")}<h1>{name}</h1>{S("p",f"pg.{k}.intro","lead")}<div class="cta-row">{wa_btn(TOPICS[k],"pg.cta","btn btn-primary")}</div></div></div></div>'''
    body = banner + f'''<section><div class="wrap block">{S("h2","pg.what")}<div class="subgrid">{subtiles}</div></div></section>
<section style="padding-top:0"><div class="wrap two"><div class="card">{S("h2","pg.ideal")}<ul class="points">{ideal}</ul></div><div class="card">{S("h2","pg.deliv")}<ul class="points">{deliv}</ul></div></div></section>
<section><div class="wrap"><div class="sec-head">{S("h2","pg.proc")}</div><div class="grid three">{steps}</div></div></section>
<section><div class="wrap"><div class="sec-head">{S("h2","pg.pairs")}</div><div class="pairs">{pairs}</div></div></section>
<section><div class="wrap narrow"><div class="sec-head">{S("h2","faq.title")}</div>{faqs}</div></section>
<section class="final"><div class="wrap">{S("h2","pg.cta")}<div class="cta-row">{wa_btn(TOPICS[k],"hero.cta","btn btn-primary")}<a class="btn btn-ghost" href="contact.html" {i("final.cta2")}>{en("final.cta2")}</a></div></div></section>'''
    PILLAR_PAGES[SLUG[k]] = page("services", f"AashiFX™ | {name}", f"{name}: {D['en'][f's.{k}.n']} by AashiFX™.", body)



# ---------- Sub-service pages ----------
SUB_PAGES = {}
for k,name,icon,*_ in PILLARS:
    lst = SUBLIST[k]
    for idx,(sid,tk,slug) in enumerate(lst):
        gets = ''.join(f'<div class="card get"><span class="tick" aria-hidden="true">✓</span><p {i(f"sub.{sid}.g{m}")}>{en(f"sub.{sid}.g{m}")}</p></div>' for m in (1,2,3))
        steps = ''.join(f'<div class="card"><p class="stepn" aria-hidden="true">{m}</p>{S("h3",f"pg.s{m}")}{S("p",f"pg.{k}.s{m}")}</div>' for m in (1,2,3))
        sibs = [lst[(idx+j) % len(lst)] for j in (1,2,3)]
        sibtiles = ''.join(f'<a class="art r43" href="{s_}.html">{img_art(s_)}<span class="cap"><b {i(t_)}>{en(t_)}</b></span></a>' for s_,t_,_ in sibs)
        banner = f'''<div class="banner">{img_art(sid, True)}<div class="over"><div class="wrap"><a class="backlink" href="{SLUG[k]}.html">{name}</a><h1 {i(tk)}>{en(tk)}</h1>{S("p",f"sub.{sid}.d","lead")}<div class="cta-row">{wa_btn(name + ": " + D["en"][tk],"pg.cta","btn btn-primary")}</div></div></div></div>'''
        body = banner + f'''<section><div class="wrap"><div class="sec-head">{S("h2","sub.get")}</div><div class="grid three">{gets}</div></div></section>
<section><div class="wrap"><div class="sec-head">{S("h2","pg.proc")}</div><div class="grid three">{steps}</div></div></section>
<section><div class="wrap"><div class="sec-head">{S("h2","sub.more")}</div><div class="grid three">{sibtiles}</div></div></section>
<section class="final"><div class="wrap">{S("h2","pg.cta")}<div class="cta-row">{wa_btn(name + ": " + D["en"][tk],"hero.cta","btn btn-primary")}<a class="btn btn-ghost" href="{SLUG[k]}.html">{name}</a></div></div></section>'''
        SUB_PAGES[sid] = page("services", f"AashiFX™ | {D['en'][tk]} · {name}", f"{D['en'][tk]}: {D['en'][f'sub.{sid}.d']}", body)

# ---------- Contact ----------
add("ct.eyebrow","Get in touch","تواصل معنا"); add("ct.title","Contact","تواصل")
add("ct.sub","WhatsApp is the fastest way. We reply there first.","واتساب أسرع وسيلة. نردّ عليك هناك أولاً.")
add("ct.topic","Pick a pillar to start the chat","اختر ركيزة لبدء المحادثة"); add("ct.num","WhatsApp and phone","واتساب وهاتف")
add("ct.reach","Serving India and the GCC.","نخدم الهند ودول الخليج.")
chips = ''.join(f'<a class="chip-link" data-wa data-wa-topic="{TOPICS[k]}" href="https://wa.me/" rel="noopener">{TOPICS[k]}</a>' for k,*_ in PILLARS)
contact = page("contact","AashiFX™ | Contact","Contact AashiFX™ on WhatsApp.",
  pbanner("page-contact","ct.eyebrow","ct.title","ct.sub")+f'''<section><div class="wrap contact">
<div class="card">{S("p","ct.num","eyebrow")}<p class="bignum" dir="ltr">+966 53 074 1843</p>{S("p","ct.reach","muted")}
<div class="cta-row" style="margin-top:1.25rem">{wa_btn("", "hero.cta", "btn btn-primary")}</div></div>
<div>{S("p","ct.topic","muted")}<div class="chips big">{chips}</div></div></div></section>''')

# ---------- About ----------
add("ab.eyebrow","About","من نحن"); add("ab.sub","Brand-to-Business Integrator. One accountable person behind every project.","مُتكامل من العلامة إلى الأعمال. شخص واحد مسؤول عن كل مشروع.")
add("ab.how","How we work","كيف نعمل")
add("ab.s1","Design","صمّم"); add("ab.s1d","Brand and concept first. Clear, strong, yours.","العلامة والفكرة أولاً. واضحة وقوية وتخصّك.")
add("ab.s2","Document","وثّق"); add("ab.s2d","Every detail on paper: quotes, scope, files.","كل التفاصيل موثّقة: العروض والنطاق والملفات.")
add("ab.s3","Deliver","سلّم"); add("ab.s3d","Ready to use, on time, with support after.","جاهز للاستخدام، في الموعد، مع دعم بعد التسليم.")
add("ab.pr","Principles","مبادئنا")
add("ab.p1","Soul","الروح"); add("ab.p1d","Every piece has a reason and a feel.","لكل عمل سبب وإحساس.")
add("ab.p2","Discipline","الانضباط"); add("ab.p2d","Clear scope, clear timeline.","نطاق واضح وجدول زمني واضح.")
add("ab.p3","Privacy","الخصوصية"); add("ab.p3d","Client work stays private.","أعمال العملاء تبقى سرّية.")
steps = ''.join(f'<div class="card"><p class="stepn" aria-hidden="true">{n}</p>{S("h3",f"ab.s{n}")}{S("p",f"ab.s{n}d")}</div>' for n in (1,2,3))
prin = ''.join(f'<div class="card">{S("h3",f"ab.p{n}")}{S("p",f"ab.p{n}d")}</div>' for n in (1,2,3))
about = page("about","AashiFX™ | About","About CHIEF™, Founder and Creative Director of AashiFX™.",
  pbanner("page-about","ab.eyebrow","about.title","ab.sub","<h1><bdi>CHIEF™</bdi></h1>")+f'''<section><div class="wrap about"><div class="avatar" aria-hidden="true"><bdi>C™</bdi></div><div>
{S("p","about.role","role")}{S("p","about.p","muted")}<ul class="points"><li {i("about.l1")}>{en("about.l1")}</li><li {i("about.l2")}>{en("about.l2")}</li><li {i("about.l3")}>{en("about.l3")}</li></ul></div></div></section>
<section><div class="wrap"><div class="sec-head">{S("h2","ab.how")}</div><div class="grid three">{steps}</div></div></section>
<section><div class="wrap"><div class="sec-head">{S("h2","ab.pr")}</div><div class="grid three">{prin}</div></div></section>''')

# ---------- Portfolio ----------
add("pf.sub","Anonymised samples. Client names stay private.","نماذج بدون أسماء. أسماء العملاء تبقى سرّية.")
for n,(a,b,c) in {1:(("Logo and colour palette","الشعار والألوان"),("Typography and usage rules","الخطوط وقواعد الاستخدام"),("Stationery and social kit","القرطاسية وحزمة التواصل")),
 2:(("Company story and values","قصة الشركة وقيمها"),("Services laid out step by step","الخدمات مرتبة خطوة بخطوة"),("Print and digital formats","نسخ للطباعة ورقمية")),
 3:(("Equipment and services overview","نظرة على المعدات والخدمات"),("Strong photo-led layout","تصميم قائم على الصور"),("Contact and credentials page","صفحة التواصل والاعتماد"))}.items():
    for m,(x,y) in enumerate((a,b,c),1): add(f"pf.w{n}.p{m}",x,y)
add("pf.more","More samples on request.","المزيد من النماذج عند الطلب."); add("pf.ask","Ask for samples","اطلب نماذج")
def work(n):
    f_ = {1:"brandx-logo-identity",2:"profile-car",3:"profile-heavy"}[n]
    return f'<article class="work-card"><a class="art r43" href="#">{img_art(f_)}<span class="cap"><b {i(f"w{n}.t")}>{en(f"w{n}.t")}</b><small {i(f"w{n}.d")}>{en(f"w{n}.d")}</small></span></a><ul class="points">' + ''.join(f'<li {i(f"pf.w{n}.p{m}")}>{en(f"pf.w{n}.p{m}")}</li>' for m in (1,2,3)) + '</ul></article>'
portfolio = page("portfolio","AashiFX™ | Portfolio","Anonymised samples of BrandX work by AashiFX™.",
  pbanner("page-portfolio","work.eyebrow","work.title","pf.sub")+f'''<section><div class="wrap"><div class="grid work">{work(1)}{work(2)}{work(3)}</div>
{S("p","pf.more","muted",' style="margin-top:1.5rem"')}<div class="cta-row" style="margin-top:1rem">{wa_btn("Portfolio samples","pf.ask","btn btn-primary")}</div></div></section>''')

# ---------- ATLAS ----------
add("at.sub","Curated headlines in English, Arabic and Tamil. Short reads, no noise.","عناوين مختارة بالإنجليزية والعربية والتاملية. قراءة قصيرة بلا ضجيج.")
add("at.note","Sample layout. Live Saudi Gazette headlines arrive with the ATLAS™ feed.","تصميم تجريبي. عناوين Saudi Gazette الحيّة تصل مع تغذية أطلس™.")
S1=("Two-line summary appears here, with the source and time.","ملخص من سطرين يظهر هنا مع المصدر والوقت.","இங்கே இரண்டு வரி சுருக்கம், மூலத்துடன் நேரமும் இடம்பெறும்.")
news={"en":("English","ltr",[("World","Sample headline: Global markets open the week"),("Tech","Sample headline: New AI tools reach small businesses"),("Business","Sample headline: Gulf construction projects keep pace")],S1[0]),
"ar":("العربية","rtl",[("العالم","عنوان تجريبي: الأسواق العالمية تفتتح الأسبوع"),("التقنية","عنوان تجريبي: أدوات ذكاء اصطناعي جديدة للشركات الصغيرة"),("الأعمال","عنوان تجريبي: مشاريع البناء في الخليج تواصل وتيرتها")],S1[1]),
"ta":("தமிழ்","ltr",[("உலகம்","மாதிரி தலைப்பு: உலகச் சந்தைகள் வாரத்தைத் தொடங்குகின்றன"),("தொழில்நுட்பம்","மாதிரி தலைப்பு: சிறு வணிகங்களுக்கு புதிய AI கருவிகள்"),("வணிகம்","மாதிரி தலைப்பு: வளைகுடா கட்டுமானத் திட்டங்கள் தொடர்கின்றன")],S1[2])}
tabs=''.join(f'<button class="tab" type="button" role="tab" data-tab="{k}" aria-selected="{"true" if k=="en" else "false"}">{v[0]}</button>' for k,v in news.items())
panes=''
for k,(lbl,d,items,s) in news.items():
    cards=''.join(f'<article class="card news"><span class="tag" style="margin:0">{t}</span><h3>{h}</h3><p>{s}</p></article>' for t,h in items)
    panes+=f'<div class="pane grid three" data-pane="{k}" lang="{k}" dir="{d}"{"" if k=="en" else " hidden"}>{cards}</div>'
SRC={"en":'Source: <a href="https://saudigazette.com.sa" rel="noopener">Saudi Gazette</a>. Arabic and Tamil versions are translations.',"ar":'المصدر: <a href="https://saudigazette.com.sa" rel="noopener">Saudi Gazette</a>. النسختان العربية والتاملية مترجمتان.',"ta":'மூலம்: <a href="https://saudigazette.com.sa" rel="noopener">Saudi Gazette</a>. அரபு, தமிழ் பதிப்புகள் மொழிபெயர்ப்புகள்.'}
panes=''
for k,(lbl,d,items,s_) in news.items():
    cards=''.join(f'<article class="card news"><span class="tag" style="margin:0">{t}</span><h3>{h}</h3><p>{s_}</p></article>' for t,h in items)
    panes+=f'<div class="pane" data-pane="{k}" lang="{k}" dir="{d}"{"" if k=="en" else " hidden"}><div class="grid three">{cards}</div><p class="srcline">{SRC[k]}</p></div>'
ahero=f'''<section class="page-hero"><div class="wrap">{S("p","atlas.eyebrow","eyebrow")}<h1 class="sr" {i("atlas.title")}>{en("atlas.title")}</h1>
<div class="atlas-panel"><img src="assets/atlas-badge.webp" width="120" height="120" alt=""><img src="assets/atlas-wordmark.webp" width="420" height="55" alt="ATLAS™"></div>
{S("p","atlas.sys","sys")}{S("p","at.sub","lead")}</div></section>'''
atlas = page("atlas","AashiFX™ | ATLAS™ Executive Intelligence","ATLAS™ by AashiFX™: Executive Intelligence. Curated news in English, Arabic and Tamil, sourced from Saudi Gazette.",
  ahero+f'<section><div class="wrap"><div class="tabs" role="tablist">{tabs}</div>{S("p","at.note","muted note")}{panes}</div></section>')

for n,h in tuple(PILLAR_PAGES.items())+tuple(SUB_PAGES.items())+(("index",index),("services",services),("contact",contact),("about",about),("portfolio",portfolio),("atlas",atlas)):
    open(R+n+".html","w").write(h)

# ---------- app.js ----------
def dump(l): return ",\n".join(f"      {json.dumps(k)}: {json.dumps(v, ensure_ascii=False)}" for k,v in D[l].items())
JS = '''/* AashiFX™ site: EN/AR toggle (RTL), WhatsApp links, ATLAS tabs. No dependencies. */
(function () {
  // WhatsApp number: country code + number, digits only
  var WA_NUMBER = "966530741843";
  var WA_TEXT = { en: "Hi AashiFX, I'd like to discuss a project.", ar: "مرحباً AashiFX، أودّ مناقشة مشروع." };

  var T = {
    en: {
%s
    },
    ar: {
%s
    }
  };

  function store(k, v) { try { if (v === undefined) return localStorage.getItem(k); localStorage.setItem(k, v); } catch (e) {} return null; }

  function selectTab(l) {
    var tabs = document.querySelectorAll("[data-tab]");
    if (!tabs.length) return;
    tabs.forEach(function (t) { t.setAttribute("aria-selected", t.getAttribute("data-tab") === l); });
    document.querySelectorAll("[data-pane]").forEach(function (p) { p.hidden = p.getAttribute("data-pane") !== l; });
  }

  function apply(lang) {
    var d = T[lang];
    document.documentElement.lang = lang;
    document.documentElement.dir = lang === "ar" ? "rtl" : "ltr";
    document.querySelectorAll("[data-i18n]").forEach(function (el) {
      var v = d[el.getAttribute("data-i18n")];
      if (v) el.textContent = v;
    });
    document.querySelectorAll("[data-wa]").forEach(function (a) {
      var topic = a.getAttribute("data-wa-topic");
      var text = WA_TEXT[lang] + (topic ? " (" + topic + ")" : "");
      a.href = "https://wa.me/" + WA_NUMBER + "?text=" + encodeURIComponent(text);
    });
    selectTab(lang);
    store("lang", lang);
  }

  var lang = store("lang");
  if (lang !== "ar" && lang !== "en") lang = (navigator.language || "").slice(0, 2) === "ar" ? "ar" : "en";
  apply(lang);

  document.addEventListener("click", function (e) {
    if (e.target.closest("[data-lang-toggle]")) { lang = lang === "en" ? "ar" : "en"; apply(lang); return; }
    if (e.target.closest("[data-theme-toggle]")) {
      var root = document.documentElement;
      var cur = root.getAttribute("data-theme") || (matchMedia("(prefers-color-scheme: light)").matches ? "light" : "dark");
      var next = cur === "light" ? "dark" : "light";
      root.setAttribute("data-theme", next);
      store("theme", next);
      return;
    }
    var tb = e.target.closest("[data-tab]");
    if (tb) { selectTab(tb.getAttribute("data-tab")); return; }
    var b = e.target.closest("[data-burger]");
    if (b) {
      var open = document.getElementById("menu").classList.toggle("open");
      b.setAttribute("aria-expanded", open);
    }
  });
})();
''' % (dump("en"), dump("ar"))
open(R+"assets/app.js","w").write(JS)

# css lives in assets/style.css (edited directly)
