--- component.ts ---
```typescript
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-open-page',
  templateUrl: './open-page.component.html',
  styleUrls: ['./open-page.component.css']
})
export class OpenPageComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }

}
```

--- component.html ---
```html
<div class="open-page">
  <div class="status-bar">
    <div class="connections">
      <div class="battery">
        <div class="border"></div>
        <div class="cap"></div>
        <div class="capacity"></div>
      </div>
      <div class="wifi">
        <div class="wifi-paths">
          <div class="wifi-path"></div>
          <div class="wifi-path"></div>
          <div class="wifi-path"></div>
        </div>
      </div>
      <div class="cellular-connection">
        <div class="cellular-connection-paths">
          <div class="cellular-connection-path"></div>
          <div class="cellular-connection-path"></div>
          <div class="cellular-connection-path"></div>
          <div class="cellular-connection-path"></div>
        </div>
      </div>
    </div>
    <div class="time">
      <div class="time-text">9:27</div>
    </div>
  </div>
  <div class="register-text">register</div>
  <div class="button">
    <div class="rectangle-2"></div>
    <div class="log-in">log in</div>
  </div>
  <div class="shape"></div>
  <div class="group">
    <div class="button register-button">
      <div class="rectangle-2 register-rectangle-2"></div>
      <div class="register register-text">register</div>
    </div>
    <div class="sapphire">SappHIRE</div>
    <div class="union">
      <div class="rectangle-2 vector"></div>
      <div class="rectangle-2-1 vector"></div>
    </div>
  </div>

  <div class="register-step-1">
    <div class="rectangle"></div>
    <div class="register-component">
      <div class="register-register">Register</div>
    </div>
    <div class="component">
      <div class="rectangle-2 component-rectangle-2"></div>
      <div class="abcd-sapphire-com">abcd@sapphire.com</div>
    </div>
     <div class="component">
      <div class="rectangle-2 component-rectangle-2"></div>
      <div class="password">••••••••••••</div>
    </div>

    <div class="button next-button">
      <div class="rectangle-2 next-rectangle-2"></div>
      <div class="next">next</div>
    </div>
    <div class="keyboard">
        <div class="background"></div>
        <div class="home-indicator">
          <div class="shape"></div>
        </div>
        <div class="keyboard-keys">
          <div class="dictation">
            <div class="mic">
              <div class="union">
                <div class="shape"></div>
                <div class="shape"></div>
                <div class="shape"></div>
              </div>
              <div class="path"></div>
              <div class="path"></div>
            </div>
          </div>
          <div class="emoji">
            <div class="emoji-inner">
              <div class="emoji-path"></div>
              <div class="emoji-path"></div>
              <div class="emoji-path"></div>
              <div class="emoji-path"></div>
              <div class="emoji-path"></div>
              <div class="emoji-path"></div>
            </div>
          </div>
          <div class="return">
            <div class="background"></div>
            <div class="return-text">return</div>
          </div>
          <div class="spacebar">
            <div class="background"></div>
            <div class="space">space</div>
          </div>
          <div class="lowercase">
            <div class="keys">
                <div class="key-123">
                    <div class="background"></div>
                    <div class="key-123-text">123</div>
                </div>
                <div class="backspace">
                  <div class="background"></div>
                  <div class="backspace-icon">
                    <div class="shape"></div>
                    <div class="shape-booleans">
                      <div class="rectangle-7"></div>
                      <div class="rectangle-7"></div>
                    </div>
                  </div>
                </div>
                <div class="shift">
                  <div class="background"></div>
                  <div class="shift-symbol">
                    <div class="combined-shape">
                      <div class="rectangle-3"></div>
                      <div class="rectangle-4"></div>
                    </div>
                  </div>
                </div>
                <div class="alphabet">
                  <div class="background"></div>
                  <div class="alphabet-text">m</div>
                </div>
                 <div class="alphabet">
                  <div class="background"></div>
                  <div class="alphabet-text">n</div>
                </div>
                 <div class="alphabet">
                  <div class="background"></div>
                  <div class="alphabet-text">b</div>
                </div>
                <div class="alphabet">
                  <div class="background"></div>
                  <div class="alphabet-text">v</div>
                </div>
                <div class="alphabet">
                  <div class="background"></div>
                  <div class="alphabet-text">c</div>
                </div>
                <div class="alphabet">
                  <div class="background"></div>
                  <div class="alphabet-text">x</div>
                </div>
                <div class="alphabet">
                  <div class="background"></div>
                  <div class="alphabet-text">z</div>
                </div>
                <div class="alphabet">
                  <div class="background"></div>
                  <div class="alphabet-text">l</div>
                </div>
                <div class="alphabet">
                  <div class="background"></div>
                  <div class="alphabet-text">k</div>
                </div>
                <div class="alphabet">
                  <div class="background"></div>
                  <div class="alphabet-text">j</div>
                </div>
                <div class="alphabet">
                  <div class="background"></div>
                  <div class="alphabet-text">h</div>
                </div>
                <div class="alphabet">
                  <div class="background"></div>
                  <div class="alphabet-text">g</div>
                </div>
                <div class="alphabet">
                  <div class="background"></div>
                  <div class="alphabet-text">f</div>
                </div>
                <div class="alphabet">
                  <div class="background"></div>
                  <div class="alphabet-text">d</div>
                </div>
                <div class="alphabet">
                  <div class="background"></div>
                  <div class="alphabet-text">s</div>
                </div>
                <div class="alphabet">
                  <div class="background"></div>
                  <div class="alphabet-text">a</div>
                </div>
                 <div class="alphabet">
                  <div class="background"></div>
                  <div class="alphabet-text">p</div>
                </div>
                 <div class="alphabet">
                  <div class="background"></div>
                  <div class="alphabet-text">o</div>
                </div>
                <div class="alphabet">
                  <div class="background"></div>
                  <div class="alphabet-text">i</div>
                </div>
                <div class="alphabet">
                  <div class="background"></div>
                  <div class="alphabet-text">u</div>
                </div>
                <div class="alphabet">
                  <div class="background"></div>
                  <div class="alphabet-text">y</div>
                </div>
                <div class="alphabet">
                  <div class="background"></div>
                  <div class="alphabet-text">t</div>
                </div>
                <div class="alphabet">
                  <div class="background"></div>
                  <div class="alphabet-text">r</div>
                </div>
                <div class="alphabet">
                  <div class="background"></div>
                  <div class="alphabet-text">e</div>
                </div>
                <div class="alphabet">
                  <div class="background"></div>
                  <div class="alphabet-text">w</div>
                </div>
                <div class="alphabet">
                  <div class="background"></div>
                  <div class="alphabet-text">q</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

<div class="login">
        <div class="rectangle"></div>
        <div class="component-inner">
          <div class="rectangle-2 component-rectangle-2"></div>
          <div class="abcd-sapphire-com">abcd@sapphire.com</div>
        </div>
        <div class="component-password">
          <div class="rectangle-2 component-rectangle-2"></div>
          <div class="password">••••••••••••</div>
        </div>

        <div class="button-1">
          <div class="rectangle-2 button-rectangle-2"></div>
          <div class="login-text">Log in</div>
        </div>
        <div class="keyboard">
            <div class="background"></div>
            <div class="home-indicator">
              <div class="shape"></div>
            </div>
            <div class="keyboard-keys">
              <div class="dictation">
                <div class="mic">
                  <div class="union">
                    <div class="shape"></div>
                    <div class="shape"></div>
                    <div class="shape"></div>
                  </div>
                  <div class="path"></div>
                  <div class="path"></div>
                </div>
              </div>
              <div class="emoji">
                <div class="emoji-inner">
                  <div class="emoji-path"></div>
                  <div class="emoji-path"></div>
                  <div class="emoji-path"></div>
                  <div class="emoji-path"></div>
                  <div class="emoji-path"></div>
                  <div class="emoji-path"></div>
                </div>
              </div>
              <div class="return">
                <div class="background"></div>
                <div class="return-text">return</div>
              </div>
              <div class="spacebar">
                <div class="background"></div>
                <div class="space">space</div>
              </div>
              <div class="lowercase">
                <div class="keys">
                    <div class="key-123">
                        <div class="background"></div>
                        <div class="key-123-text">123</div>
                    </div>
                    <div class="backspace">
                      <div class="background"></div>
                      <div class="backspace-icon">
                        <div class="shape"></div>
                        <div class="shape-booleans">
                          <div class="rectangle-7"></div>
                          <div class="rectangle-7"></div>
                        </div>
                      </div>
                    </div>
                    <div class="shift">
                      <div class="background"></div>
                      <div class="shift-symbol">
                        <div class="combined-shape">
                          <div class="rectangle-3"></div>
                          <div class="rectangle-4"></div>
                        </div>
                      </div>
                    </div>
                    <div class="alphabet">
                      <div class="background"></div>
                      <div class="alphabet-text">m</div>
                    </div>
                     <div class="alphabet">
                      <div class="background"></div>
                      <div class="alphabet-text">n</div>
                    </div>
                     <div class="alphabet">
                      <div class="background"></div>
                      <div class="alphabet-text">b</div>
                    </div>
                    <div class="alphabet">
                      <div class="background"></div>
                      <div class="alphabet-text">v</div>
                    </div>
                    <div class="alphabet">
                      <div class="background"></div>
                      <div class="alphabet-text">c</div>
                    </div>
                    <div class="alphabet">
                      <div class="background"></div>
                      <div class="alphabet-text">x</div>
                    </div>
                    <div class="alphabet">
                      <div class="background"></div>
                      <div class="alphabet-text">z</div>
                    </div>
                    <div class="alphabet">
                      <div class="background"></div>
                      <div class="alphabet-text">l</div>
                    </div>
                    <div class="alphabet">
                      <div class="background"></div>
                      <div class="alphabet-text">k</div>
                    </div>
                    <div class="alphabet">
                      <div class="background"></div>
                      <div class="alphabet-text">j</div>
                    </div>
                    <div class="alphabet">
                      <div class="background"></div>
                      <div class="alphabet-text">h</div>
                    </div>
                    <div class="alphabet">
                      <div class="background"></div>
                      <div class="alphabet-text">g</div>
                    </div>
                    <div class="alphabet">
                      <div class="background"></div>
                      <div class="alphabet-text">f</div>
                    </div>
                    <div class="alphabet">
                      <div class="background"></div>
                      <div class="alphabet-text">d</div>
                    </div>
                    <div class="alphabet">
                      <div class="background"></div>
                      <div class="alphabet-text">s</div>
                    </div>
                    <div class="alphabet">
                      <div class="background"></div>
                      <div class="alphabet-text">a</div>
                    </div>
                     <div class="alphabet">
                      <div class="background"></div>
                      <div class="alphabet-text">p</div>
                    </div>
                     <div class="alphabet">
                      <div class="background"></div>
                      <div class="alphabet-text">o</div>
                    </div>
                    <div class="alphabet">
                      <div class="background"></div>
                      <div class="alphabet-text">i</div>
                    </div>
                    <div class="alphabet">
                      <div class="background"></div>
                      <div class="alphabet-text">u</div>
                    </div>
                    <div class="alphabet">
                      <div class="background"></div>
                      <div class="alphabet-text">y</div>
                    </div>
                    <div class="alphabet">
                      <div class="background"></div>
                      <div class="alphabet-text">t</div>
                    </div>
                    <div class="alphabet">
                      <div class="background"></div>
                      <div class="alphabet-text">r</div>
                    </div>
                    <div class="alphabet">
                      <div class="background"></div>
                      <div class="alphabet-text">e</div>
                    </div>
                    <div class="alphabet">
                      <div class="background"></div>
                      <div class="alphabet-text">w</div>
                    </div>
                    <div class="alphabet">
                      <div class="background"></div>
                      <div class="alphabet-text">q</div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

      </div>
```

--- component.css ---
```css
.open-page {
  width: 375px;
  height: 812px;
  background: #fff;
  overflow: hidden;
  position: relative;
}

.status-bar {
  position: absolute;
  left: 0;
  top: 0;
  width: 100%;
  height: 44px;
}

.connections {
  position: absolute;
  top: 0;
  right: 0;
  width: 68px;
  height: 16px;
}

.battery {
  position: absolute;
  top: 0;
  right: 0;
  width: 25px;
  height: 12px;
}

.battery .border {
  position: absolute;
  top: 0;
  left: 0;
  width: 22px;
  height: 11.33px;
  border: 1px solid #000;
  opacity: 0.35;
  border-radius: 2.67px;
}

.battery .cap {
  position: absolute;
  top: 0;
  right: 0;
  width: 1.33px;
  height: 4px;
  opacity: 0.4;
  background: #000;
}

.battery .capacity {
  position: absolute;
  top: 0;
  left: 0;
  width: 18px;
  height: 7.33px;
  background: #000;
  border-radius: 1.33px;
}

.wifi {
  position: absolute;
  top: 0;
  right: 28px;
  width: 21px;
  height: 15px;
}

.wifi-paths {
    position: absolute;
  top: 0;
  left: 0;
  width: 15.33px;
  height: 11px;
  right: 111px;
  opacity: 0.85;
}

.cellular-connection {
 position: absolute;
  top: 0;
  right: 50px;
  width: 68px;
  height: 16px;
}

.cellular-connection-paths {
    position: absolute;
  top: 0;
  left: 0;
  width: 17px;
  height: 10.67px;
}


.time {
    position: absolute;
  top: 0;
  left: 0;
  width: 56px;
  height: 23px;
}

.time .time-text {
 position: absolute;
  top: 0;
  left: 0;
  width: 54px;
  height: 18px;
  color: #000;
  text-align: center;
  font: 600 15px "SF Pro Text", sans-serif;
  letter-spacing: -0.33px;
}

.register-text {
 position: absolute;
  top: 493px;
  left: 50%;
  transform: translateX(-50%);
  font: bold 13px "SF Pro Text", sans-serif;
  letter-spacing: -0.2px;
  text-transform: uppercase;
}

.button {
  position: absolute;
  left: 50%;
  top: 491px;
  transform: translateX(-50%);
  width: 167px;
  height: 52px;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}

.button .rectangle-2 {
position: absolute;
  top: 0;
  left: 0;
  width: 167px;
  height: 52px;
  border: 2px solid #521515;
  background-color: #fff;
  border-radius: 6px;
}

.button .log-in {
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  font: bold 13px "Roboto", sans-serif;
  letter-spacing: 0.52px;
  text-transform: uppercase;
  color: #521515;
}

.shape {
 position: absolute;
  top: 563px;
  left: 50%;
  transform: translateX(-50%);
  width: 135px;
  height: 5px;
  background: #000;
  border-radius: 10px;
}

.group {
 position: absolute;
  top: 66px;
  left: 50%;
  transform: translateX(-50%);
  width: 290.5px;
  height: 477px;
}

.group .button.register-button {
position: absolute;
  top: 491px;
  left: 50%;
  transform: translateX(-50%);
  width: 167px;
  height: 52px;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}

.group .button.register-button .rectangle-2.register-rectangle-2 {
 position: absolute;
  top: 0;
  left: 0;
  width: 167px;
  height: 52px;
  background-color: #521515;
  border: none;
  border-radius: 6px;
}

.group .button .register.register-text {
  color: #fff;
}

.group .sapphire {
 position: absolute;
  top: 143px;
  left: 50%;
  transform: translateX(-50%);
  font: normal 48px "Coda", sans-serif;
  letter-spacing: -0.72px;
  color: #521515;
}

.group .union {
  position: absolute;
  top: 66px;
  left: 0;
  width: 53.5px;
  height: 48px;
  transform: rotate(180deg);
  background: #000;
}

/* Styling for Registration step 1*/
.register-step-1 {
  position: absolute;
  left: 100px;
  top: -236px;
  width: 375px;
  height: 812px;
  background: #fff;
}

/* Styling for the Login step */
.login {
  position: absolute;
  left: 634px;
  top: -236px;
  width: 375px;
  height: 812px;
  background: #fff;
}
```