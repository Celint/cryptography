from gmpy2 import invert

n = 18690335923587401272274452704481360570172985404580539063800068051656440429429871365395054315640752532296947368692114470225356692536524400977654869148032388125799309218663204697229664909011485587613365452585032596764275491277414697481105851773647161610402132026691775916016553018682069701165441563008827995352611081377270870961993003013204177040058543233755687401404873980918055496287658034651227141717469285207476056572349778123328897009744634817496098394061315284815254961151320468094310039820962531035968267268268010725856858309162679460701018490649742399223523025603196989203376520552712234103945686235851168704197
e1 = 45587
c1 = 16167727758903996576096559905875720098288126746947881348559884301049169706633745162775381231934848926926336723901304757405550229637817214484023955969693035894957966351062499960322888308805168362517446917049096915775716196800955160000385416365405410955562564500477809756411948523651424710882522252905725748929443870283229342832288940132373133197184822137736727920615873015907008217881547535972413173476550578516400328091416902875237572234574721113400553149371512093446768725217512524403757536906085963949582413442515091370824510062191706642044495556872139543680579549734066433918086034435641616054060560954568232712018
e2 = 46703
c2 = 4051256362678668941591389649707196306648815239760451573743728048044775910843378801571775912749185991932895311555108409267492028822060776715413179384279670263628511282730373355447340800556239071004370666379540564144864151234895131782878581913072907048432171347128883376391790409009420746298338784561119194541235318537650998570442677179478314199563112285328599040930099684822745080889988191274487041116661793076165537004671221924681424548529631390031337534654001726336839258868722613984396546883769274511872655962122756975201432017205996340237474298384556312742800406095847839843336893163373492539899465821326534644935

# 求乘法逆元
def getGcd(a, b):
    if b == 0:
        return 1, 0
    else:
        k = a // b
        r = a % b
        x1, y1 = getGcd(b, r)
        x, y = y1, x1 - k * y1
        return x, y

s1, s2 = getGcd(e1, e2)
print(s1, s2)
print(e1 * s1 + e2 * s2)
if s1 < 0:
    s1 = -s1
    c1 = invert(c1, n)
elif s2 < 0:
    s2 = - s2
    c2 = invert(c2, n)
print(c1, c2)

m = pow(c1, s1, n) * pow(c2, s2, n) % n
print(m)