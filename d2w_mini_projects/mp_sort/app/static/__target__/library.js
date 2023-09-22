// Transcrypt'ed from Python, 2023-09-22 13:53:50
var random = {};
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, abs, all, any, assert, bool, bytearray, bytes, callable, chr, copy, deepcopy, delattr, dict, dir, divmod, enumerate, filter, float, getattr, hasattr, input, int, isinstance, issubclass, len, list, map, max, min, object, ord, pow, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
import * as __module_random__ from './random.js';
__nest__ (random, '', __module_random__);
var __name__ = '__main__';
export var gen_random_int = function (number, seed) {
	var ls = [];
	for (var i = 0; i < number; i++) {
		ls.append (i);
	}
	random.seed (seed);
	random.shuffle (ls);
	return ls;
};
export var generate = function () {
	var number = 10;
	var seed = 200;
	var array = gen_random_int (number, seed);
	var array_str = ','.join (map (str, array));
	array_str += '.';
	document.getElementById ('generate').innerHTML = array_str;
};
export var sortnumber1 = function () {
	var ls_str = document.getElementById ('generate').innerHTML;
	var ls_str = ls_str.__getslice__ (0, -(1), 1);
	var ls_str = ls_str.py_split (',');
	var ls_int = list (map (int, ls_str));
	var n = len (ls_int);
	var swapped = true;
	while (swapped) {
		var swapped = false;
		var new_n = 0;
		for (var idx = 1; idx < n; idx++) {
			if (ls_int [idx - 1] > ls_int [idx]) {
				var __left0__ = tuple ([ls_int [idx], ls_int [idx - 1]]);
				ls_int [idx - 1] = __left0__ [0];
				ls_int [idx] = __left0__ [1];
				var swapped = true;
				var new_n = idx;
			}
		}
		var n = new_n;
	}
	var array_str = ','.join (map (str, ls_int));
	document.getElementById ('sorted').innerHTML = array_str;
};
export var sortnumber2 = function () {
	var value = document.getElementsByName ('numbers') [0].value;
	if (value == '') {
		window.alert ('Your textbox is empty');
		return ;
	}
	else {
		var array_str = value.py_split (',');
		for (var i = 0; i < len (array_str); i++) {
			array_str [i] = int (array_str [i].strip ());
		}
		var insertion_sort = function (ls) {
			var n = range (len (ls));
			for (var i of tuple ([1, n])) {
				if (ls [i] > ls [i - 1]) {
					var __left0__ = tuple ([ls [i - 1], ls [i]]);
					ls [i] = __left0__ [0];
					ls [i - 1] = __left0__ [1];
				}
				else {
					continue;
				}
			}
			var strg = str (ls);
			return strg;
		};
	}
	var array_str = insertion_sort (array_str);
	document.getElementById ('sorted').innerHTML = array_str;
};

//# sourceMappingURL=library.map