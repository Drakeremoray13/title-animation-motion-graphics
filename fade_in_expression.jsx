// Smooth fade-in animation for film titles
// Apply to Opacity property

var fadeInTime = 1.5;  // Duration of fade in seconds
var holdTime = 3.0;    // Time to hold at full opacity

if (time < fadeInTime) {
  // Smooth ease-in curve
  var t = time / fadeInTime;
  100 * (t * t * (3 - 2 * t));  // Smoothstep function
} else if (time < fadeInTime + holdTime) {
  100;  // Full opacity
} else {
  // Optional fade out
  var fadeOutStart = fadeInTime + holdTime;
  var fadeOutDuration = 1.0;
  var fadeT = (time - fadeOutStart) / fadeOutDuration;
  100 * Math.max(0, 1 - fadeT);
}
