// Bouncing animation expression for After Effects
// Apply to Position property for dynamic bounce effect

var amp = 30;        // Amplitude of bounce
var freq = 2.5;      // Frequency of bounce
var decay = 4;       // Decay rate of bounce

if (numKeys > 0) {
  var n = key(numKeys).time;
  var t = time - n;
  
  if (t > 0) {
    // Create bouncing effect with exponential decay
    value + [0, amp * Math.sin(freq * t * 2 * Math.PI) / Math.exp(decay * t)];
  } else {
    value;
  }
} else {
  value;
}
