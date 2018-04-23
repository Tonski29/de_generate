from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from settings import DB_URL, HOME_DIR

engine = create_engine(DB_URL, echo=True) #
Base = declarative_base()
Session = sessionmaker(bind=engine)

# classes are the components that popultae the table ord efine anoilies
class Scenario(Base):
    __tablename__ = "scenarios"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    credentials = relationship("Credential")
    web_history = relationship("EvidenceWebHistory")
    web_downloads = relationship("EvidenceWebDownload")
    files = relationship("EvidenceFile")


class Credential(Base):
    __tablename__ = "credentials"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    scenario = Column(Integer, ForeignKey('scenarios.id'))


class EvidenceWebHistory(Base):
    __tablename__ = "web_history"

    id = Column(Integer, primary_key=True)
    url = Column(String)
    incriminating = Column(Boolean)
    scenario = Column(Integer, ForeignKey('scenarios.id'))

class EvidenceWebDownload(Base):
    __tablename__ = "web_downloads"

    id = Column(Integer, primary_key=True)
    url = Column(String)
    file_path = Column(String)
    incriminating = Column(Boolean)
    scenario = Column(Integer, ForeignKey('scenarios.id'))


class EvidenceFile(Base):
    __tablename__ = "files"

    id = Column(Integer, primary_key=True)
    file_path = Column(String)
    contents = Column(String)
    scenario = Column(Integer, ForeignKey('scenarios.id'))


def init_db(): # engine is used to build the db
    Base.metadata.create_all(engine)


def seed_db():
    session = Session()
    #Scenarios
    scenario_murder = Scenario(name="murder")
    scenario_blackmail = Scenario(name="blackmail")
    scenario_drugs =Scenario(name="drugs")
    session.add_all([scenario_murder, scenario_blackmail, scenario_drugs])
    session.commit()

    scenario_murder = session.query(Scenario).filter_by(name="murder").first()
    scenario_blackmail = session.query(Scenario).filter_by(name="blackmail").first()
    scenario_drugs = session.query(Scenario).filter_by(name="drugs").first()

    #EvidenceFiles these files are hard coded and assigned/ delted/hidden or encrypted after being commited to db based
    # on random num generation

    murder_files = []

    murder_files.append(EvidenceFile(file_path=HOME_DIR+"Documents/Secret/plot.txt",
                           contents="Under the darkness of night I shall murder them my cheating b wife and drew",
                           scenario=scenario_murder.id))

    murder_files.append(EvidenceFile(file_path=HOME_DIR + "/Diary.txt",
                                contents="she forced me to do it, i cant believe she would do this to me 1/4/18",
                                scenario=scenario_murder.id))
    murder_files.append(EvidenceFile(file_path="/disposal.txt",
                                   contents="I plan on burying both in applecross, nice and far from me",
                                   scenario=scenario_murder.id))
    murder_files.append(EvidenceFile(file_path="/disposal.txt",
                               contents="clean up scene, borrow a car, get rid and report missing persons",
                               scenario=scenario_murder.id))
    murder_files.append(EvidenceFile(file_path="/usr/todo.txt",
                               contents="clean up scene, borrow a car, get rid and report missing persons",
                               scenario=scenario_murder.id))

    blackmail_files = []

    blackmail_files.append(EvidenceFile(file_path="/usr/todo.txt",
                                   contents="I know what you've done, everyone's done something",
                                   scenario=scenario_blackmail.id))
    blackmail_files.append(EvidenceFile(file_path=HOME_DIR+"state.txt",
                                   contents="I found a large amount of big data at work which i can sell for $$$$",
                                   scenario=scenario_blackmail.id))
    blackmail_files.append(EvidenceFile(file_path=HOME_DIR + "Documents/threat.txt",
                                    contents="To Big-Data Inc, £20,000 by Thursday May ORELSE!",
                                    scenario=scenario_blackmail.id))
    blackmail_files.append(EvidenceFile(file_path="/var/spool/cups/tmp/backup.txt",
                                    contents="If Big D wont sell i need to access tor network to sell.",
                                    scenario=scenario_blackmail.id))
    blackmail_files.append(EvidenceFile(file_path="/end.txt",
                                 contents="After i make all this money from blackmail, im going to Italy, oh yeah.",
                                 scenario=scenario_blackmail.id))
    drug_files = []

    drug_files.append(EvidenceFile(file_path="/var/local/offer.txt",
                                   contents='for 1 week only 3g for the price of 2 on bubblegum',
                                   scenario=scenario_drugs.id))
    drug_files.append(EvidenceFile(file_path="/var/spool/cups/tmp/cust.txt",
                                    contents='cal=2b dave=6j dijon=21i tiny-toe=15j',
                                    scenario=scenario_drugs.id))
    drug_files.append(EvidenceFile(file_path="/sbin.yield.txt",
                                    contents='2 j plants = 4oz, 2 b plants = 4.5oz , 2 i plants =1.75oz est = £700',
                              scenario=scenario_drugs.id))
    drug_files.append(EvidenceFile(file_path=HOME_DIR+"Documents/business/debt.txt",
                             contents='andy = £20, michael = £80 danny =£65',
                             scenario=scenario_drugs.id))
    drug_files.append(EvidenceFile(file_path=HOME_DIR + "Documents/contacts.txt",
                                  contents='rickyd =07477424235, Neil = 07816450513, Billy = 01259781254 = pricey/available',
                                  scenario=scenario_drugs.id))

    murder_web = []
    murder_web.append(EvidenceWebHistory(url="https://bbc.co.uk/",
                                         incriminating=False,
                                         scenario=scenario_murder))
    murder_web.append(EvidenceWebHistory(url="https://www.lastminute.com/holidays/honeymoon-destinations.html",
                                         incriminating=False,
                                         scenario=scenario_murder))
    murder_web.append(EvidenceWebHistory(url="https://www.google.co.uk/search?q=i+think+my+gf+is+cheating+on+me&oq=i+think+my+gf+is+cheating+on+me&aqs=chrome..69i57.6943j0j4&sourceid=chrome&ie=UTF-8",
                                         incriminating=False,
                                         scenario=scenario_murder))
    murder_web.append(EvidenceWebHistory(url="https://www.google.co.uk/search?q=when+are+limp+bozkit+in+town%3F&oq=when+are+limp+bozkit+in+town%3F&aqs=chrome..69i57.5833j0j4&sourceid=chrome&ie=UTF-8",
                                         incriminating=False,
                                         scenario=scenario_murder))
    murder_web.append(EvidenceWebHistory(url="http://putlockers.net/episode/how-to-get-away-with-murder-4x1/",
                                         incriminating=False,
                                         scenario=scenario_murder))
    murder_web.append(EvidenceWebHistory(url="http://putlockers.net/episode/how-to-get-away-with-murder-4x2/",
                                         incriminating=False,
                                         scenario=scenario_murder))
    murder_web.append(EvidenceWebHistory(url="http://putlockers.net/episode/how-to-get-away-with-murder-4x3/",
                                         incriminating=False,
                                         scenario=scenario_murder))
    murder_web.append(EvidenceWebHistory(url="https://www.aftermath.com/content/requirements-for-crime-scene-cleanup",
                                         incriminating=True,
                                         scenario=scenario_murder))
    murder_web.append(EvidenceWebHistory(url="https://www.google.co.uk/search?q=how+to+clean+up+bloodstains&oq=how+to+clean+up+bloodstains&aqs=chrome..69i57.6563j0j1&sourceid=chrome&ie=UTF-8",
                                         incriminating=True,
                                         ))
    murder_web.append(EvidenceWebHistory(url="http://www.cracked.com/blog/5-creative-ways-people-got-revenge-cheating-spouses/",
                                         incriminating=True,
                                         scenario=scenario_murder))
    murder_web.append(EvidenceWebHistory(url="http://www.cracked.com/blog/5-creative-ways-people-got-revenge-cheating-spouses/",
                                         incriminating=True,
                                         scenario=scenario_murder))
    murder_web.append(EvidenceWebHistory(url="http://whatculture.com/science/10-ways-to-dispose-of-a-dead-body-if-you-really-needed-to",
                                         incriminating=True,
                                         scenario=scenario_murder))
    drug_web = []
    drug_web.append(EvidenceWebHistory(url="https://www.travelrepublic.co.uk/1-63966-2-0/holidays-in-amsterdam?oid=285250&mkid=424647245&aid=1&dev=c&adid=256025489191&targetid=kwd-106236909&gclid=EAIaIQobChMI27GmtPrG2gIVQUkYCh1LwAQqEAAYAiAAEgK78_D_BwE",
                                         incriminating=False,
                                         scenario=scenario_drugs))
    drug_web.append(EvidenceWebHistory(url="http://uk.businessinsider.com/health-benefits-of-medical-marijuana-2014-4",
                                       incriminating=False,
                                       scenario=scenario_drugs))
    drug_web.append(EvidenceWebHistory(url="https://www.ticketweb.co.uk/music/reggae/1258/events",
                                       incriminating=False,
                                       scenario=scenario_drugs))
    drug_web.append(EvidenceWebHistory(url="https://www.savethestudent.org/make-money/10-quick-cash-injections.html",
                                       incriminating=False,
                                       scenario=scenario_drugs))
    drug_web.append(EvidenceWebHistory(url="https://www.linuxbabe.com/browser/install-tor-browser-6-0-4-ubuntu-16-04",
                                       incriminating=False,
                                       scenario=scenario_drugs))
    drug_web.append(EvidenceWebHistory(url="https://sensiseeds.com/en/feminized-seeds",
                                       incriminating=True,
                                       scenario=scenario_drugs))
    drug_web.append(EvidenceWebHistory(url="https://www.how-to-marijuana.com/buy-marijuana-grow-box.html",
                                       incriminating=True,
                                       scenario=scenario_drugs))
    drug_web.append(EvidenceWebHistory(url="https://www.google.co.uk/search?q=uk+how+to+get+a+pistol&oq=uk+how+to+get+a+pistol&aqs=chrome..69i57j69i64l3.8721j0j4&sourceid=chrome&ie=UTF-8",
                                       incriminating=True,
                                       scenario=scenario_drugs))
    drug_web.append(EvidenceWebHistory(url="https://www.quora.com/How-can-I-not-get-caught-dealing-drugs?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa",
                                       incriminating=True,
                                       scenario=scenario_drugs))
    drug_web.append(EvidenceWebHistory(url="https://topdocumentaryfilms.com/how-to-sell-drugs/",
                                       incriminating=True,
                                       scenario=scenario_drugs))
    black_web = []
    black_web.append(EvidenceWebHistory(url="https://packaging.python.org/guides/installing-using-pip-and-virtualenv/",
                                        scenario=scenario_blackmail))
    black_web.append(EvidenceWebHistory(url="https://topdocumentaryfilms.com/how-to-sell-drugs/",
                                        incriminating=False,
                                        scenario=scenario_blackmail))
    black_web.append(EvidenceWebHistory(url="https://benmccormick.org/2014/07/14/learning-vim-in-2014-configuring-vim/",
                                        incriminating=False,
                                        scenario=scenario_blackmail))
    black_web.append(EvidenceWebHistory(url="https://fossbytes.com/best-linux-distros-for-programming-developers/",
                                        incriminating=False,
                                        scenario=scenario_blackmail))
    black_web.append(EvidenceWebHistory(url="http://watchamericandad.net/",
                                        incriminating=False,
                                        scenario=scenario_blackmail))
    black_web.append(EvidenceWebHistory(url="https://www.youtube.com/watch?v=furTlhb-990",
                                        incriminating=False,
                                        scenario=scenario_blackmail))
    black_web.append(EvidenceWebHistory(url="http://www.newsweek.com/secretive-world-selling-data-about-you-4647890",
                                        incriminating=True,
                                        scenario=scenario_blackmail))
    black_web.append(EvidenceWebHistory(url="https://www.google.co.uk/search?q=how+to+blackmail+an+employer&oq=how+to+blackmail+an+employer&aqs=chrome..69i57.7669j0j4&sourceid=chrome&ie=UTF-8",
                                        incriminating=True,
                                        scenario=scenario_blackmail))
    black_web.append(EvidenceWebHistory(url="http://www.nchsoftware.com/voicechanger/index.html",
                                        incriminating=True,
                                        scenario=scenario_blackmail))
    black_web.append(EvidenceWebHistory(url="https://wildleaks.org/install-tor-bundle-stay-anonymous/",
                                        incriminating=True,
                                        scenario=scenario_blackmail))
    black_web.append(EvidenceWebHistory(url="https://www.wikihow.com/Bribe-Someone",
                                        incriminating=True,
                                        scenario=scenario_blackmail))
    #generic_hist[]

    drug_down = []
    drug_down.append(EvidenceWebDownload(url='http://www.eluniversal.com.mx/sites/default/files/styles/f03-651x400/public/2017/10/06/destinos-museo_del_cannabis-marihuana.jpg?itok=-r8ohf0C&c=975fc0c961167b3465df283dd06bb3a8',
                                           file_path = '/drive2',
                                           incriminating =False,
                                           scenario=scenario_blackmail))


    #session.add_all([murder_plot, murder_confession, blackmail_draft, new_prices])
    session.add_all(drug_down)
    session.add_all(murder_web)
    session.add_all(murder_files)
    session.add_all(blackmail_files)
    session.add_all(drug_files)
    session.add_all(drug_down)

    session.commit()

