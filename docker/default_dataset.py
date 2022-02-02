#!/usr/bin/env python3

# 1000 observations of 4 * ((2 * random.random() - 1) ^ 3 + 1)
# 
# quantile(data, c(0.50, 0.85, 0.95, 0.99))
#      50%      85%      95%      99% 
# 4.000051 5.583405 7.016093 7.774128 
#

data = [
    3.978136260258965,
    5.7285258905249785,
    7.8916256292077325,
    2.0799680137559764,
    4.07825157907109,
    3.9944564719858433,
    1.5545416236117213,
    3.9446531407204453,
    5.324474468005935,
    4.296488736318588,
    4.504960186052406,
    3.9999199660740743,
    6.321757552756517,
    2.328954379258905,
    0.6560599608784989,
    4.162349106427695,
    4.079091761098617,
    4.228120755013392,
    3.2326016085906355,
    4.028844369350724,
    1.1891985616000325,
    3.9945459022527685,
    2.2140224474431554,
    1.1781818058602278,
    4.00082233660447,
    4.870613955532999,
    7.057406640202236,
    4.927931020200264,
    0.26923936529229975,
    6.990701402744474,
    3.896118943029982,
    5.754924296549737,
    3.9999547978153474,
    4.1676454009461095,
    0.21727986175462854,
    3.9999683003302446,
    2.8449170514272764,
    3.280804148345977,
    3.9993574499548914,
    0.3811743286670106,
    4.000298933389786,
    1.6117073328925708,
    1.2531934737700503,
    4.16356811693794,
    6.080864483610989,
    0.3734188459315746,
    4.001984646307083,
    1.044542745377043,
    4.406054400457106,
    4.491713924688657,
    3.9999879507376677,
    3.7817171465605526,
    5.421132346357493,
    5.065915357654494,
    4.341490087617851,
    3.0969438990900704,
    4.036607352533848,
    3.995623172866634,
    5.0920429005326975,
    4.222299057919169,
    4.190251292009057,
    2.934050234288714,
    4.252481698866167,
    2.7806440344523624,
    4.0000009270349235,
    4.230891018440355,
    3.5595687105763756,
    3.6624815890264064,
    1.5519330382685972,
    0.3278519323003213,
    4.00008443734237,
    3.999949097800292,
    3.1253706732189395,
    4.137283324761577,
    3.8769857864997643,
    4.071154612126224,
    4.011171355811235,
    4.357614329928625,
    3.999270801875726,
    2.65669126705333,
    6.542631100573033,
    4.124828633362816,
    2.4328120299250564,
    2.1681527641723046,
    4.012323084987188,
    3.909114276822553,
    2.2799181591513147,
    4.492349125831107,
    5.490694232541364,
    4.000145304645437,
    3.473348085853067,
    5.38040849201477,
    4.146203320565109,
    0.982129687217836,
    5.2117088803205815,
    6.24070371578748,
    0.54654219826537,
    7.685704771021316,
    0.6895219648001487,
    3.9990868235249266,
    4.000519013018976,
    4.93677852918427,
    3.987201226773958,
    7.570920230544216,
    4.0002346100246235,
    3.991788547569194,
    4.039159374157971,
    2.7716179830335004,
    3.9038759189045478,
    3.3933520317936194,
    3.8909570996367537,
    3.6335625049411338,
    3.9709390367048645,
    1.783402273615767,
    6.729306673607445,
    7.143089845077797,
    4.0105339565090485,
    4.0557098827595395,
    3.9907112561360414,
    4.00001069833231,
    1.673317416058083,
    3.9010969880984083,
    4.01035387889941,
    5.0880161527132,
    3.996169180620519,
    7.394387703863042,
    2.980519459787777,
    1.01830825764115,
    3.7731416220527105,
    7.513959773783208,
    4.000037884982237,
    4.107359605643895,
    3.8642651126748033,
    7.7973060904353595,
    2.9640168072065034,
    4.902600470707856,
    2.455259340414732,
    4.135346588139762,
    2.1810244438358737,
    3.8061179002602685,
    4.97842246880758,
    4.89127195428647,
    0.3169937789902919,
    2.6039081957915005,
    7.391802135125449,
    3.553852989859164,
    3.9005308621721935,
    4.016891902862282,
    3.9451800201742633,
    5.681475344042622,
    3.714303522330381,
    4.394286917881169,
    3.9802890201097973,
    0.9730809230066164,
    4.637933435525012,
    6.528461608254391,
    7.990109087605826,
    3.455911865844376,
    4.733242456263528,
    4.36642669199711,
    3.1519177299654544,
    0.6165988547447001,
    3.918253944943249,
    6.169247223109448,
    4.057020663198432,
    4.987327872622382,
    3.4207321730797045,
    3.9970421230312105,
    4.3764475146457,
    3.5910399580386496,
    4.42145258914767,
    4.026718863089902,
    3.310535670507762,
    1.9767214615534443,
    4.000000067902834,
    5.190017073854365,
    6.252469042011667,
    2.670400426704439,
    1.2305173809402907,
    3.3078279634122087,
    3.4608994893476432,
    3.614539266806664,
    3.9010229359385473,
    4.115820708786075,
    1.986773019827551,
    3.8647498254755317,
    3.6691862399102573,
    6.0936560757150495,
    3.9858071808221833,
    7.747009034516246,
    3.8704193518894434,
    4.653942422037787,
    3.9753753228603785,
    4.122038424463445,
    7.103997977842687,
    4.663900240168238,
    3.351786233565951,
    3.5830433633253214,
    4.310139572133814,
    5.433549486523669,
    4.0089604942701405,
    1.8025760887305657,
    5.8108117497762715,
    5.702159367775822,
    4.87558813701847,
    3.6636468643753304,
    3.974617339077806,
    3.292179016090458,
    4.186281411255469,
    3.492004058063965,
    6.9462699442758025,
    7.398812224862154,
    4.106591727540207,
    6.811108254730446,
    3.093258095623417,
    4.2037809987387424,
    4.2660672376375315,
    3.994415582911153,
    0.997504308510027,
    2.5542264321545236,
    3.88960451545777,
    0.9910457595496607,
    4.000131993711885,
    3.2462306086215547,
    0.07664329949156823,
    4.312627478879877,
    7.092943545067328,
    4.05851570760072,
    3.9971043587972748,
    4.032721996622833,
    3.8994289678258207,
    4.94622215682694,
    3.985753272241266,
    3.2114195878862564,
    5.873920399644308,
    4.029375154989625,
    4.0550967421987965,
    7.044004080220638,
    4.410623049638167,
    7.550782859153695,
    1.2574125589081229,
    3.463706809703616,
    5.818333516462194,
    4.677509744077318,
    3.7660391070239108,
    3.999865338679995,
    4.123158209070299,
    3.971739641669454,
    1.9212266138233391,
    4.782815172604461,
    0.9666417898526509,
    6.04564950345055,
    3.802477773172089,
    2.3651632439212293,
    3.235203515558946,
    1.844789501563418,
    1.0867419380908259,
    4.217514585698656,
    3.553623578228669,
    5.814816118079382,
    6.341447701639995,
    4.33686500232718,
    3.8322626205277515,
    7.223583642580397,
    6.3321827514297215,
    4.7069382958125345,
    3.0592911457126615,
    4.181147593821322,
    0.517485622759358,
    4.262957525754586,
    3.8216564577860623,
    4.736531776478172,
    2.5235936748803356,
    0.8607752393293242,
    0.523128790674523,
    5.860062631428207,
    4.000210605242014,
    6.524840911464041,
    4.006310462262484,
    6.680154197004379,
    3.6334852632510923,
    1.0645925794390991,
    6.380052284408681,
    4.003604854909569,
    6.701052233707294,
    4.0078817197587675,
    5.244732635440023,
    3.992393224604028,
    4.950744637998696,
    4.001134534794074,
    1.3696034161035833,
    1.256885830935473,
    4.0167132286485945,
    4.663498672536484,
    4.429098498985898,
    0.49575353583724047,
    4.005631739717695,
    5.247582369043814,
    3.5232739021765536,
    4.061710502852589,
    3.9087357011958757,
    6.394353753161756,
    4.049406951797655,
    4.889692193845076,
    3.5160418111037686,
    2.716471167607467,
    7.607487727000773,
    3.193607077001328,
    0.5994234749991323,
    5.816469331844029,
    2.077427467978795,
    3.9973441747969387,
    4.000017985761946,
    4.70867605988397,
    4.002834533108514,
    4.045290534933072,
    3.2281698674292443,
    3.9999959094061244,
    6.886325209994067,
    3.9976601091105377,
    3.014383576185785,
    0.4490024535947028,
    5.048022848868964,
    3.965276942476675,
    5.869031959491966,
    4.62368913005086,
    6.037372442462607,
    3.822918507522958,
    4.000228150309824,
    4.000260278209888,
    0.12910355590944578,
    2.2201533374692737,
    5.59353412628502,
    3.988105772349059,
    4.611205950180705,
    2.954452112411989,
    3.4075396480091054,
    2.263001443067153,
    3.5247831705512382,
    7.677999395621541,
    0.41036046123740144,
    3.901262588104086,
    4.404657330150786,
    2.3986279740272654,
    7.34682862085717,
    3.7107580259702764,
    3.9997572030348447,
    5.343129788734687,
    6.055381577810738,
    4.857332411599723,
    6.383634947799511,
    4.459464728796728,
    4.0093079767502005,
    2.5651213577463547,
    3.187684881096326,
    3.999986816114576,
    4.016018465569707,
    3.8452261383470177,
    4.214659840449595,
    2.1907274539562174,
    3.8891811873933593,
    2.8084089734462756,
    5.624698550462136,
    1.9548790175466584,
    0.6214706304549256,
    1.9848671321386253,
    3.996842858380322,
    3.632693871295603,
    4.008764407539943,
    3.979670382276172,
    3.818615741042101,
    0.8898805724149463,
    3.3603725320654867,
    3.998787438683582,
    3.931519616523815,
    4.00006131443235,
    4.072575515479272,
    4.144396731810588,
    3.071759682539219,
    7.18857129358057,
    0.25926507607903915,
    4.002411839378979,
    3.915311578779722,
    2.7292496487968148,
    2.589513223018638,
    7.132245740488051,
    3.891967628948255,
    7.8348791291603925,
    4.032610282397803,
    0.8722458784257063,
    7.175636460612674,
    1.3034335040858025,
    3.530195098580497,
    6.374608241513561,
    3.9885875747756554,
    4.201550277799696,
    4.040400664271156,
    5.230205625836876,
    3.999080036854311,
    5.922102750366095,
    1.826308468666996,
    1.5843119574230164,
    6.7467387181877605,
    4.738940192938098,
    4.012066502607641,
    6.54189270057756,
    3.9997134216528556,
    4.0205463802460555,
    3.992577584914316,
    3.7951302226991044,
    0.43804587289904084,
    6.838978080800997,
    3.9004650736929007,
    4.817290228604225,
    4.060476348090243,
    6.787988876221753,
    1.4477210787843737,
    0.42480285333413725,
    3.969114539635169,
    4.002031962521525,
    5.543151205687193,
    2.8042495924835107,
    3.936284041637232,
    4.131074926987355,
    5.367600313661912,
    3.9510484360745295,
    2.845428901165757,
    6.974905844354547,
    1.4338295118199236,
    4.394106692268989,
    3.921891820305226,
    4.001174305817168,
    4.651284292308304,
    4.01387551420864,
    3.305439210482679,
    3.9541547537400508,
    4.050430282163028,
    3.8771063695598875,
    4.473762985168145,
    3.96976343699065,
    3.9984622242436525,
    5.843484220512459,
    1.1408311016970654,
    3.907884173941424,
    3.118014752452158,
    0.4204784919712736,
    3.905525992055029,
    4.164961264831073,
    4.768022276344827,
    2.736378667509813,
    4.2975532624425785,
    3.360594066696928,
    3.9813406509763576,
    3.850218889465842,
    3.6519958472226577,
    0.2753191802096193,
    5.947768497472903,
    4.004216766223205,
    0.23705775620320235,
    4.21993533631391,
    0.4655094121196317,
    7.017943596545306,
    4.61099948724305,
    4.0548381629270445,
    5.597798013092653,
    3.9729758775125537,
    3.9940896240472847,
    3.9931450976700433,
    6.715515694503843,
    3.5639468008424218,
    2.4332511225091045,
    0.06882067894161858,
    3.267177458934302,
    4.330610484013787,
    6.140824028370565,
    2.701507488248769,
    6.692756818970474,
    5.238618049091767,
    3.8461476493449016,
    4.034825416133538,
    6.7733312138090245,
    4.008348244991202,
    0.15385600599520322,
    4.231463487796116,
    4.136377474149459,
    3.9999657170473055,
    0.8569061109021652,
    0.08142646689510569,
    4.380811960946415,
    3.3742743195741953,
    4.0349459693182865,
    4.168225348751795,
    3.999813533754525,
    4.222052551480738,
    5.6920106995938715,
    2.52789807449532,
    5.166249467446695,
    2.7590392062731297,
    3.9999482560017796,
    4.5386234703092825,
    6.465457012744026,
    2.9020850805105076,
    0.29174448743828973,
    5.246089434366753,
    6.189576455194928,
    4.028576804110986,
    3.9247272255141707,
    6.579161446379446,
    3.947710176798679,
    4.1733316097209086,
    4.5734774032261125,
    3.6220608931765836,
    3.59237861141451,
    4.000004111121838,
    5.436731065194815,
    3.6004773233103973,
    4.925241932218745,
    5.637976790915311,
    0.2880813859429816,
    5.581991217864154,
    2.381064751728466,
    3.2803324027522063,
    3.9998667671985517,
    1.4971393075976263,
    1.3853506622530043,
    4.399937924164933,
    7.956269337558791,
    4.00039778566535,
    5.968132859817415,
    5.352444693592705,
    2.337546027847707,
    3.995970637809315,
    2.706480333419397,
    6.005172892804718,
    1.0327282156758106,
    4.213900091440806,
    3.984652079834047,
    4.075086010574257,
    3.992574931732418,
    3.992058100029684,
    5.292314923846005,
    1.8972514925956006,
    1.3069028838978505,
    4.486646190388932,
    2.053351887068539,
    3.8831639577246846,
    3.999999846536055,
    4.241651762173194,
    4.041728168003382,
    3.7921943806789584,
    3.5587706541111017,
    5.572823798975799,
    4.015888883896895,
    4.391209439337191,
    7.005764621552224,
    4.278986052997958,
    0.439266318990549,
    7.415305704908734,
    4.88775215952139,
    2.7517448618440516,
    6.21152221156288,
    0.20744034828890712,
    4.011556801349351,
    6.384550653199819,
    2.909190601892273,
    3.652698132989373,
    4.2066162098632525,
    6.2385899479897295,
    3.9992008888032937,
    4.216433356061196,
    2.632144918331526,
    4.684052243760723,
    4.9292165468133184,
    4.016018011597547,
    4.0057289813948485,
    3.008331282459368,
    7.855152223907423,
    3.985243785498238,
    4.000070730471548,
    3.9997144510040137,
    3.95967292648519,
    3.9982226457760266,
    7.558805715331006,
    5.046056055509169,
    3.8890749073103987,
    5.1085716655207305,
    1.8574892770920406,
    4.977244047931894,
    4.130404985717691,
    1.5911243304072475,
    3.997079356769504,
    4.6133434625245835,
    3.993480945071666,
    4.019509553781139,
    7.363639724953352,
    3.751488378948704,
    5.495556187008798,
    3.9999969323759275,
    4.60383662161112,
    4.008491601144949,
    2.1669177899146614,
    3.944291296681041,
    4.272362260546,
    4.7837782971420575,
    3.9797730165276524,
    3.7262786246645185,
    4.107777845165485,
    3.50909992647174,
    3.613326231107472,
    4.005500590712573,
    7.8719332033488545,
    5.813996691268752,
    5.47849018063611,
    6.479355957648501,
    2.3337111622056455,
    3.976178536228939,
    3.9992904894384074,
    3.6291476972253287,
    4.418970764417433,
    4.459984812620376,
    2.5350486652898523,
    3.7749568540384284,
    4.009544936175546,
    4.341562162593685,
    4.000306936835775,
    3.9999972009422273,
    4.925806699055366,
    4.619226379914758,
    3.9394624405983363,
    4.151338493655858,
    4.311340463140328,
    4.6568020372685925,
    3.077555398715908,
    4.000989693485371,
    1.4216757336655927,
    6.6471573948301,
    4.016856584242656,
    3.2827339117226453,
    2.7113418226883095,
    6.783042076315574,
    1.5663820889088558,
    7.868804637835729,
    4.13434223271468,
    3.951883250929333,
    4.21987186351052,
    3.592766073283089,
    6.658489635811389,
    3.7586127680992245,
    0.8380118697616012,
    4.007190819956036,
    4.652044262751236,
    3.702535836305983,
    3.8860982854064754,
    4.186022803617535,
    2.174393835713971,
    4.3882188122478265,
    4.02279171401127,
    4.1137358363505605,
    3.4156422984394332,
    4.180360089808367,
    4.00343879199443,
    5.294089814349716,
    3.9785649039772206,
    4.412432045965882,
    4.237386041159185,
    3.9914123930113936,
    3.998528893475377,
    6.5443294895292485,
    2.052303665200303,
    3.9999120394023695,
    4.026125880886352,
    3.9534778540143742,
    5.373326300474936,
    1.7923200823174708,
    5.601171480174573,
    2.933724612020204,
    4.082042266719502,
    4.521924794713312,
    3.9962828413997387,
    2.9653333230611114,
    4.407030428987559,
    4.853052792162211,
    3.5878392139579205,
    1.057569873039923,
    3.8979902897274026,
    7.995547444941431,
    5.591415967155183,
    3.998683136980303,
    2.7974734842228584,
    7.556452502121294,
    3.272807208890343,
    3.9276570505065065,
    6.222688241816492,
    3.435236909748177,
    2.9408269578246653,
    4.770953748542163,
    4.2026702891811585,
    3.793967304563089,
    4.041287514622801,
    3.2367550148672803,
    4.103533848199351,
    3.3042681727044174,
    0.7541751479790295,
    4.007515899160703,
    2.1823596115334984,
    2.8904462996814546,
    6.107501038533632,
    1.465463016032536,
    3.8494489049662257,
    6.588348275702969,
    4.034716752222384,
    4.1034991397701255,
    3.7599531776481725,
    4.763304843624761,
    4.373024503992529,
    3.9924665274020366,
    7.465685575282706,
    5.484821682403961,
    4.001332903100398,
    0.10030403845599434,
    6.693000620129258,
    3.9997262791047383,
    4.4576891968154255,
    2.3603682610880563,
    5.219444072751683,
    3.9913298050529757,
    1.96685671322013,
    3.9462300239729915,
    6.982860074243197,
    5.497907500911935,
    6.075695906253877,
    7.675675876606856,
    4.001968453039744,
    4.005486707112783,
    4.18549681335184,
    7.075255438475407,
    4.195932859569584,
    3.5707079508023205,
    4.031064767401034,
    4.0004529918636536,
    3.8689729710426364,
    2.8514450319306563,
    4.189172629946228,
    4.074463327356701,
    2.1720224366834633,
    4.262514903319841,
    3.9998216722757833,
    3.809982142468185,
    3.694854856302546,
    3.8497800279227867,
    3.990207485555465,
    4.865032485504612,
    4.076941945834456,
    6.135721708450701,
    4.201708709876691,
    3.4663745884500052,
    3.888826934753468,
    3.9996288986350756,
    4.1265596496292805,
    7.10778656911747,
    6.266567751237974,
    4.233050090411557,
    5.617774918871378,
    3.7678650916406324,
    4.658180979774292,
    3.7679192448128433,
    4.29420634347784,
    4.321885203340415,
    0.9727505882160092,
    4.230371491550573,
    2.8088035194098326,
    6.775264083248141,
    4.000663362997237,
    4.482167410841565,
    4.317516590847891,
    1.0064601505514719,
    4.598471285155683,
    3.780969502683648,
    1.2823072246079752,
    4.000000000797915,
    4.000071475441857,
    7.7305414248139925,
    3.682005584089043,
    3.5382971562702723,
    1.7167486722067093,
    0.1858064473717258,
    4.853752704021568,
    4.11411392804039,
    2.3980730532271624,
    5.168254079606504,
    5.410385898448395,
    4.1390188476158905,
    5.668742523750261,
    3.6712787776790208,
    3.780263808830565,
    4.364058518660204,
    2.2524475449676373,
    0.3295732194025711,
    7.059103464777166,
    3.7502279183009604,
    3.1755490663931814,
    4.001716154444122,
    7.564714963905029,
    3.9999597938376166,
    6.102501670525365,
    0.9467314097316137,
    5.4740227187261965,
    0.10205234597952328,
    7.773893420510616,
    4.386467500631945,
    4.840194998868427,
    4.090903519068084,
    4.002803282488948,
    7.299127358576012,
    3.974742302006025,
    1.616289546268737,
    3.96009278053705,
    7.015995510597621,
    4.487224372886275,
    4.3022780291451515,
    5.698768834879581,
    5.064194130939807,
    3.107540903799253,
    6.026205333503709,
    4.000206114717048,
    2.733388007832894,
    4.865743038597467,
    5.1073538787444575,
    3.0579907227255076,
    3.9953855929956297,
    1.9863726205535022,
    4.06584989658355,
    4.0092062509863435,
    4.000000000100541,
    3.9999204010706175,
    4.020954233824588,
    4.605085598145831,
    4.377409991905652,
    4.714069277665274,
    5.727045335689944,
    4.619928403411156,
    5.257070577261019,
    0.6662083662745162,
    4.9732555864487304,
    7.44509416083471,
    5.716371086301228,
    4.004350256513784,
    7.5272027811969915,
    2.131168672286588,
    6.050136826560851,
    4.002715223062816,
    2.8993576519847393,
    4.313369718506612,
    4.094819207145057,
    3.6642332630071124,
    1.4615222497046902,
    3.2300967515610286,
    3.879168861966582,
    3.919412472384662,
    7.645319470515943,
    4.3310403304389995,
    4.048482776948399,
    2.40963855653984,
    3.9997705079998798,
    3.9566597937159,
    3.994386527173803,
    3.2205008725251543,
    4.645282383071545,
    2.613352604494721,
    4.374127711020113,
    4.646481427048543,
    3.913460947691221,
    3.979012138925693,
    2.024771313919727,
    3.9577656687178844,
    3.479753172823175,
    7.773710276073926,
    3.9996883113589656,
    2.8803980514881937,
    4.239586041824578,
    2.0687260654392983,
    3.9759454393120546,
    2.7170610148946865,
    4.176000309569059,
    3.8929591643514243,
    5.816249400546529,
    4.047119491197286,
    4.741382782419525,
    4.06188077483528,
    2.851702764632882,
    3.4221990687625876,
    4.644422075593994,
    3.8229121022719874,
    4.649448467506518,
    5.685910477954728,
    7.914624890500344,
    3.9998996030960203,
    4.009658727253316,
    4.029314155440513,
    4.757792453319636,
    3.859876968386967,
    3.9996717424261212,
    2.043701309488204,
    4.686724331757033,
    3.9631868582402126,
    3.8467824344704167,
    1.9511045113542118,
    4.002619605841742,
    3.8039232866261115,
    1.1381006989306521,
    4.880053888923651,
    0.9441401810304795,
    5.860113864150421,
    3.9999997709965682,
    4.000040258839616,
    5.623327967251025,
    3.7930396617795568,
    5.9961594635555855,
    3.66995675319221,
    3.7977561611089112,
    4.0021079684927505,
    3.985719434658351,
    4.852938306391533,
    2.604557909268947,
    7.720537339696529,
    2.7524550004735544,
    1.778516796783649,
    6.7965002776666035,
    3.1643491498659575,
    4.000351183830865,
    4.0183041842654665,
    2.249156975996837,
    1.713518327828632,
    2.5103062040657558,
    3.9618474784077327,
    5.165959122150287,
    5.028043580795219,
    4.184735029943476,
    3.999422045051325,
    1.6507435666089307,
    4.000089663579459,
    3.608910155131557,
    4.060890601765865,
    3.994405196714274,
    5.067860526581874,
    5.546149090811927,
    2.162852729368482,
    6.481877976229603,
    4.743027498410761,
    3.759600712763247,
    4.751730850625247,
    3.9770432650106624,
    3.9999850482655925,
    3.999225632219839,
    3.4773113901982056,
    5.97780170705477,
    4.679732360220991,
    3.998716969594324,
    3.950960853135656,
    2.1715245725569496,
    7.7246336555403765,
    3.9999999999864695,
    3.760625867100076,
    3.341673874060997,
    3.9999543743239947,
    3.8000038442761284,
    3.975863883742236,
    4.983815182050462,
    3.9920498321362086,
    4.594233969180708,
    5.888039590641901,
    3.159327160190191,
    2.66127453249795,
    4.181551494136233,
    4.009732181504051,
    5.983156273186035,
    3.9745363726752636,
    3.985720142801922,
    3.999858890953345,
    0.5062937353365609,
    3.9457270999720864,
    4.037831627674695,
    2.3863972130451914,
    3.327511127854846,
    3.957387184304849,
    5.625704719433167,
    4.0100249372143475,
    4.802258080027865,
    0.17009388840682638,
    3.2090851650829215,
    5.459490672458253,
    3.9986879745508834,
    5.892036249592794,
    3.999634457889437,
    3.5576475378088848,
    3.9905119908537294,
    4.011739281764012,
    4.541207378091374,
    4.0407720522457655,
    3.1949573731909995
    ]


if __name__ == '__main__':
    for v in data:
        print(v)