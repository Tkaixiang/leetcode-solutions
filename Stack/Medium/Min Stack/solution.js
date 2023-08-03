// https://leetcode.com/problems/min-stack/description/?envType=study-plan-v2&envId=top-100-liked

class MinStack {
    constructor() {
        this.arrayStack = []
        this.minStack = [] // ======= MINIMUM STACK =======
    }

    push(val) {
        this.arrayStack.push(val)
        if (this.minStack.length === 0 || val <= this.minStack[this.minStack.length - 1]) this.minStack.push(val)
    }
    pop() {
        const poppedValue = this.arrayStack.pop()
        if (poppedValue === this.minStack[this.minStack.length - 1]) this.minStack.pop()
    }
    top() {
        return this.arrayStack[this.arrayStack.length - 1]
    }
    getMin() {
        return this.minStack[this.minStack.length - 1]
        /* 
        minStack works as the mainstructure is a STACK
        - Not every element needs to be included as
        - Every element bigger than the Current Minimum will be removed before it reaches the next minimum
        - E.g -1 -5 -3 (Although -3 is the 2nd minimum it has to be removed if we want to remove -5 as the minimum)
        */ 
    }
}
/** 
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(val)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */