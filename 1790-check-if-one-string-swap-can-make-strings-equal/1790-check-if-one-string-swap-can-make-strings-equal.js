var areAlmostEqual = function(s1, s2) {
    let diff = [];

    for (let i = 0; i < s1.length; i++) {
        if (s1[i] !== s2[i]) {
            diff.push(i);
        }
    }

    if (diff.length === 0) return true;
    if (diff.length !== 2) return false;

    let a = diff[0];
    let b = diff[1];

    return s1[a] === s2[b] && s1[b] === s2[a];
};