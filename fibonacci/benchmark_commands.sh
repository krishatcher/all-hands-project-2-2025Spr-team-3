echo " - -- --- ---- START ---- --- -- -"
echo " ~~~ ~~~ ~~~ Test 1 ~~~ ~~~ ~~~"
poetry run fibonacci --quantity 7 --approach iterative
echo ""
echo " ~~~ ~~~ ~~~ Test 2 ~~~ ~~~ ~~~"
poetry run fibonacci --quantity 14 --approach iterative
echo ""
echo " ~~~ ~~~ ~~~ Test 3 ~~~ ~~~ ~~~"
poetry run fibonacci --quantity 28 --approach iterative
echo ""
echo " ~~~ ~~~ ~~~ Test 4 ~~~ ~~~ ~~~"
poetry run fibonacci --quantity 7 --approach recursive
echo ""
echo " ~~~ ~~~ ~~~ Test 5 ~~~ ~~~ ~~~"
poetry run fibonacci --quantity 14 --approach recursive
echo ""
echo " ~~~ ~~~ ~~~ Test 6 ~~~ ~~~ ~~~"
poetry run fibonacci --quantity 28 --approach recursive
echo ""
echo " ~~~ ~~~ ~~~ Test 7 ~~~ ~~~ ~~~"
poetry run fibonacci --quantity 7 --approach memoization
echo ""
echo " ~~~ ~~~ ~~~ Test 8 ~~~ ~~~ ~~~"
poetry run fibonacci --quantity 14 --approach memoization
echo ""
echo " ~~~ ~~~ ~~~ Test 9 ~~~ ~~~ ~~~"
poetry run fibonacci --quantity 28 --approach memoization
echo " - -- --- ---- END ---- --- -- -"
